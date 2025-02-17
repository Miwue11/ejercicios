/*
 Ajedrez Completo Corregido
 - Representación de tablero en matriz 8x8
 - Movimientos completos con:
   * Peones (doble paso, captura diagonal, en passant, promoción)
   * Torres, Caballos, Alfiles, Dama y Rey
   * Enroque (corto y largo)
 - Detección de jaque y jaque mate
 - CORRECCIÓN PRINCIPAL:
   isValidMove(...) ahora recibe el color 'moverColor' de la pieza
   en lugar de usar 'currentPlayer' internamente.
*/

document.addEventListener("DOMContentLoaded", () => {
    const boardElement = document.getElementById("chessboard");
  
    // Tablero 8x8
    //   r,n,b,q,k,b,n,r (minúsculas) = negras
    //   R,N,B,Q,K,B,N,R (mayúsculas) = blancas
    //   '.' = vacío
    let board = [
      ["r","n","b","q","k","b","n","r"], // 0: negras
      ["p","p","p","p","p","p","p","p"], // 1
      [".",".",".",".",".",".",".","."], // 2
      [".",".",".",".",".",".",".","."], // 3
      [".",".",".",".",".",".",".","."], // 4
      [".",".",".",".",".",".",".","."], // 5
      ["P","P","P","P","P","P","P","P"], // 6
      ["R","N","B","Q","K","B","N","R"]  // 7: blancas
    ];
  
    // Turno actual: 'w' (blancas) o 'b' (negras)
    let currentPlayer = 'w';
    // Fin de partida
    let gameOver = false;
  
    // Captura al paso y enroques
    let enPassantTarget = null;
    let castlingRights = {
      wK: true,  // Rey blanco sin mover
      wR0: true, // Torre blanca col=0 sin mover
      wR7: true, // Torre blanca col=7 sin mover
      bK: true,
      bR0: true,
      bR7: true
    };
  
    let selectedSquare = null; // { row, col }
  
    // Devuelve 'w', 'b' o null según la pieza
    function pieceColor(p) {
      if (p === ".") return null;
      return (p === p.toUpperCase()) ? 'w' : 'b';
    }
  
    // Dibuja la matriz board en el contenedor HTML
    function drawBoard() {
      boardElement.innerHTML = "";
      for (let row = 0; row < 8; row++) {
        for (let col = 0; col < 8; col++) {
          const sqDiv = document.createElement("div");
          sqDiv.classList.add("square", ((row+col)%2===0)? "light":"dark");
          sqDiv.dataset.row = row;
          sqDiv.dataset.col = col;
  
          const piece = board[row][col];
          if (piece !== ".") {
            sqDiv.textContent = toUnicode(piece);
          }
          boardElement.appendChild(sqDiv);
        }
      }
    }
  
    // Convierte p (r,n,b,q,k,p...) a símbolo Unicode
    function toUnicode(p) {
      const map = {
        'r':'♜','n':'♞','b':'♝','q':'♛','k':'♚','p':'♟',
        'R':'♖','N':'♘','B':'♗','Q':'♕','K':'♔','P':'♙'
      };
      return map[p] || p;
    }
  
    // Verifica si (r,c) está dentro del tablero
    function inBounds(r, c) {
      return (r>=0 && r<8 && c>=0 && c<8);
    }
  
    // Genera todos los movimientos (PSEUDO-LEGALES) de una pieza en (row,col)
    // SIN revisar si dejan al propio rey en jaque
    function generateMovesForSquare(row, col) {
      const p = board[row][col];
      if (p===".") return [];
      const color = pieceColor(p);
      const moves = [];
      const directionsKnight = [
        [-2,-1],[-2,1],[2,-1],[2,1],[-1,-2],[-1,2],[1,-2],[1,2]
      ];
      const directionsRook = [[1,0],[-1,0],[0,1],[0,-1]];
      const directionsBishop = [[1,1],[1,-1],[-1,1],[-1,-1]];
      const directionsKing = [
        [1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]
      ];
  
      switch(p.toUpperCase()) {
        case 'P': {
          // Peón
          const forward = (color==='w')? -1 : 1;
          const startRank = (color==='w')? 6 : 1;
  
          // Paso simple
          const fr = row + forward;
          if (inBounds(fr, col) && board[fr][col]===".") {
            moves.push({start:{r: row,c: col}, end:{r: fr,c: col}});
            // Doble paso
            if (row===startRank) {
              const fr2 = row + 2*forward;
              if (inBounds(fr2,col) && board[fr2][col]===".") {
                moves.push({start:{r: row,c: col}, end:{r: fr2,c: col}, special:'double'});
              }
            }
          }
          // Capturas diagonales
          for (let dc of [-1,1]) {
            const cc = col+dc;
            if (inBounds(fr,cc) && board[fr][cc]!=="." && pieceColor(board[fr][cc])!==color) {
              moves.push({start:{r: row,c: col}, end:{r: fr,c: cc}});
            }
          }
          // En passant
          if (enPassantTarget) {
            const {row: epRow, col: epCol} = enPassantTarget;
            // Si fr===epRow, y col +/- 1===epCol
            if (fr===epRow && Math.abs(epCol-col)===1) {
              moves.push({start:{r: row,c: col}, end:{r: epRow,c: epCol}, special:'enpassant'});
            }
          }
          break;
        }
        case 'N': { // Caballo
          for (let d of directionsKnight) {
            const nr = row+d[0], nc = col+d[1];
            if (inBounds(nr,nc) && pieceColor(board[nr][nc])!==color) {
              moves.push({start:{r: row,c: col}, end:{r: nr,c: nc}});
            }
          }
          break;
        }
        case 'R': { // Torre
          for (let d of directionsRook) {
            let nr=row, nc=col;
            while(true) {
              nr+=d[0]; nc+=d[1];
              if (!inBounds(nr,nc)) break;
              if (pieceColor(board[nr][nc])===color) break;
              moves.push({start:{r: row,c: col}, end:{r: nr,c: nc}});
              if (pieceColor(board[nr][nc])!==null) break; 
            }
          }
          break;
        }
        case 'B': { // Alfil
          for (let d of directionsBishop) {
            let nr=row, nc=col;
            while(true) {
              nr+=d[0]; nc+=d[1];
              if (!inBounds(nr,nc)) break;
              if (pieceColor(board[nr][nc])===color) break;
              moves.push({start:{r: row,c: col}, end:{r: nr,c: nc}});
              if (pieceColor(board[nr][nc])!==null) break;
            }
          }
          break;
        }
        case 'Q': { // Dama = Torre + Alfil
          const dirs = [...directionsRook, ...directionsBishop];
          for (let d of dirs) {
            let nr=row, nc=col;
            while(true) {
              nr+=d[0]; nc+=d[1];
              if (!inBounds(nr,nc)) break;
              if (pieceColor(board[nr][nc])===color) break;
              moves.push({start:{r: row,c: col}, end:{r: nr,c: nc}});
              if (pieceColor(board[nr][nc])!==null) break;
            }
          }
          break;
        }
        case 'K': { // Rey
          // Mov. normal (1 casilla)
          for (let d of directionsKing) {
            const nr = row+d[0], nc = col+d[1];
            if (inBounds(nr,nc) && pieceColor(board[nr][nc])!==color) {
              moves.push({start:{r: row,c: col}, end:{r: nr,c: nc}});
            }
          }
          // Enroque
          // Comprobamos que el rey y la torre no se hayan movido y que no estén atacadas las casillas de paso
          // + No puede enrocar si el rey está en jaque
          if (color==='w') {
            // Rey blanco en (7,4) normalmente
            if (row===7 && col===4) {
              // Enroque corto
              if (castlingRights.wK && castlingRights.wR7) {
                if (board[7][5]==='.' && board[7][6]==='.' &&
                    !isSquareAttacked(7,4,'w') && 
                    !isSquareAttacked(7,5,'w') && 
                    !isSquareAttacked(7,6,'w')) {
                  moves.push({start:{r:7,c:4}, end:{r:7,c:6}, special:'castleShort'});
                }
              }
              // Enroque largo
              if (castlingRights.wK && castlingRights.wR0) {
                if (board[7][1]==='.' && board[7][2]==='.' && board[7][3]==='.' &&
                    !isSquareAttacked(7,4,'w') &&
                    !isSquareAttacked(7,3,'w') &&
                    !isSquareAttacked(7,2,'w')) {
                  moves.push({start:{r:7,c:4}, end:{r:7,c:2}, special:'castleLong'});
                }
              }
            }
          } else {
            // Rey negro en (0,4) normalmente
            if (row===0 && col===4) {
              // Enroque corto
              if (castlingRights.bK && castlingRights.bR7) {
                if (board[0][5]==='.' && board[0][6]==='.' &&
                    !isSquareAttacked(0,4,'b') &&
                    !isSquareAttacked(0,5,'b') &&
                    !isSquareAttacked(0,6,'b')) {
                  moves.push({start:{r:0,c:4}, end:{r:0,c:6}, special:'castleShort'});
                }
              }
              // Enroque largo
              if (castlingRights.bK && castlingRights.bR0) {
                if (board[0][1]==='.' && board[0][2]==='.' && board[0][3]==='.' &&
                    !isSquareAttacked(0,4,'b') &&
                    !isSquareAttacked(0,3,'b') &&
                    !isSquareAttacked(0,2,'b')) {
                  moves.push({start:{r:0,c:4}, end:{r:0,c:2}, special:'castleLong'});
                }
              }
            }
          }
          break;
        }
      }
      return moves;
    }
  
    // Devuelve TODOS los movimientos pseudo-legales de 'color'
    function generateAllMoves(color) {
      const moves = [];
      for (let r=0; r<8; r++) {
        for (let c=0; c<8; c++) {
          if (pieceColor(board[r][c])===color) {
            const sqMoves = generateMovesForSquare(r,c);
            moves.push(...sqMoves);
          }
        }
      }
      return moves;
    }
  
    // Indica si (row,col) está atacado por el bando enemigo de 'colorUnderAttack'
    function isSquareAttacked(row, col, colorUnderAttack) {
      const enemy = (colorUnderAttack==='w')? 'b':'w';
      // Generar todos los movimientos pseudo-legales del enemigo
      const enemyMoves = generateAllMoves(enemy);
      // Si alguno termina en (row,col), significa que está atacado
      return enemyMoves.some(m => (m.end.r===row && m.end.c===col));
    }
  
    // Aplica un movimiento en el board (sin chequear jaque)
    function makeMove(move) {
      const {start, end, special} = move;
      const piece = board[start.r][start.c];
      const captured = board[end.r][end.c];
  
      board[end.r][end.c] = piece;
      board[start.r][start.c] = ".";
  
      // Actualiza enPassant
      if (special==='double') {
        // Se movió un peón 2 casillas
        const middleRow = (start.r + end.r)/2;
        enPassantTarget = {row: middleRow, col: start.c};
      } else {
        enPassantTarget = null;
      }
  
      // En passant
      if (special==='enpassant') {
        // Si piece = 'P' y se mueve a end.r, end.c, la pieza negra está en end.r+1
        if (piece==='P') {
          // Captura peón negro
          board[end.r+1][end.c] = ".";
        } else if (piece==='p') {
          board[end.r-1][end.c] = ".";
        }
      }
  
      // Promoción
      if ((piece==='P' && end.r===0) || (piece==='p' && end.r===7)) {
        // Promovemos siempre a Dama para simplificar
        board[end.r][end.c] = (piece==='P')? 'Q':'q';
      }
  
      // Enroque
      if (special==='castleShort') {
        if (piece==='K') {
          // Rey blanco: mover torre de (7,7) a (7,5)
          board[end.r][5] = 'R';
          board[end.r][7] = '.';
        } else if (piece==='k') {
          board[end.r][5] = 'r';
          board[end.r][7] = '.';
        }
      } else if (special==='castleLong') {
        if (piece==='K') {
          board[end.r][3] = 'R';
          board[end.r][0] = '.';
        } else if (piece==='k') {
          board[end.r][3] = 'r';
          board[end.r][0] = '.';
        }
      }
  
      // Actualiza derechos de enroque, etc.
      updateCastlingRights(piece, start, end);
  
      return { piece, captured, special };
    }
  
    // Deshace el movimiento
    function undoMove(move, data) {
      const {start, end, special} = move;
      const {piece, captured} = data;
  
      board[start.r][start.c] = piece;
      board[end.r][end.c] = captured;
  
      // En passant
      if (special==='enpassant') {
        if (piece==='P') {
          board[end.r+1][end.c] = 'p';
        } else if (piece==='p') {
          board[end.r-1][end.c] = 'P';
        }
      }
  
      // Enroque
      if (special==='castleShort') {
        if (piece==='K') {
          board[start.r][7] = 'R';
          board[start.r][5] = '.';
        } else if (piece==='k') {
          board[start.r][7] = 'r';
          board[start.r][5] = '.';
        }
      } else if (special==='castleLong') {
        if (piece==='K') {
          board[start.r][0] = 'R';
          board[start.r][3] = '.';
        } else if (piece==='k') {
          board[start.r][0] = 'r';
          board[start.r][3] = '.';
        }
      }
    }
  
    // Quita los derechos de enroque si Rey/Torre se movió
    function updateCastlingRights(piece, start, end) {
      const c = pieceColor(piece); // 'w' o 'b'
      if (piece.toUpperCase() === 'K') {
        if (c==='w') {
          castlingRights.wK = false;
          castlingRights.wR0 = false;
          castlingRights.wR7 = false;
        } else {
          castlingRights.bK = false;
          castlingRights.bR0 = false;
          castlingRights.bR7 = false;
        }
      }
      if (piece.toUpperCase() === 'R') {
        if (c==='w') {
          // Torre blanca a la izq
          if (start.r===7 && start.c===0) castlingRights.wR0=false;
          // Torre blanca a la der
          if (start.r===7 && start.c===7) castlingRights.wR7=false;
        } else {
          if (start.r===0 && start.c===0) castlingRights.bR0=false;
          if (start.r===0 && start.c===7) castlingRights.bR7=false;
        }
      }
    }
  
    // Comprueba si 'color' está en jaque
    function isInCheck(color) {
      // Encuentra el rey de 'color'
      let kingPos=null;
      for (let r=0; r<8; r++){
        for (let c=0; c<8; c++){
          const p = board[r][c];
          if (p!=="." && pieceColor(p)===color && p.toUpperCase()==='K') {
            kingPos={r,c};
            break;
          }
        }
        if (kingPos) break;
      }
      if (!kingPos) return false;
      return isSquareAttacked(kingPos.r, kingPos.c, color);
    }
  
    // Genera todos los movimientos de 'color'; si con uno no queda en jaque -> puede salvarse
    function canMove(color) {
      const allMoves = generateAllMoves(color);
      for (let mv of allMoves) {
        const moveData = makeMove(mv);
        if (!isInCheck(color)) {
          undoMove(mv, moveData);
          return true;
        }
        undoMove(mv, moveData);
      }
      return false;
    }
  
    // -- CORRECCIÓN IMPORTANTE --
    // 'moverColor' = color de la pieza que se mueve ( 'w' o 'b' )
    // Evitamos usar la variable global 'currentPlayer' aquí.
    // Retorna true si es lógicamente válido (sin chequear jaque).
    function isValidMovePseudo(startSquare, endSquare, moverColor) {
      const sR = startSquare.r, sC = startSquare.c;
      const eR = endSquare.r, eC = endSquare.c;
      const piece = board[sR][sC];
      if (!piece || pieceColor(piece)!==moverColor) return false; // No coincide el color
  
      // Pseudo-moves generados para esta pieza
      const pseudoMoves = generateMovesForSquare(sR, sC);
      // Ver si endSquare coincide
      return pseudoMoves.some(pm => pm.end.r===eR && pm.end.c===eC);
    }
  
    // Intenta mover la pieza de (start) a (end) en el turno actual.
    // Si deja al propio rey en jaque, se revierte.
    function tryMove(start, end) {
      const piece = board[start.r][start.c];
      const color = pieceColor(piece);
      if (!piece || color!==currentPlayer) return false;
  
      // 1) Revisar pseudo-legalidad (sin jaque)
      if (!isValidMovePseudo(start, end, color)) {
        return false;
      }
      // 2) Encontrar el 'moveObj'
      const all = generateMovesForSquare(start.r, start.c);
      const moveObj = all.find(m => m.end.r===end.r && m.end.c===end.c);
  
      // 3) Hacerlo
      const moveData = makeMove(moveObj);
  
      // 4) Si quedo en jaque, es ilegal -> revertir
      if (isInCheck(color)) {
        undoMove(moveObj, moveData);
        return false;
      }
  
      // 5) Si fue legal, cambiar turno
      const prevPlayer = currentPlayer;
      currentPlayer = (currentPlayer==='w'? 'b':'w');
  
      // 6) Ver si el nuevo jugador está en jaque
      if (isInCheck(currentPlayer)) {
        alert(`Jaque a las ${currentPlayer==='w'? 'blancas':'negras'}!`);
        // 7) ¿Jaquemate?
        if (!canMove(currentPlayer)) {
          alert(`¡Jaque mate! Ganan las ${prevPlayer==='w'?'blancas':'negras'}.`);
          gameOver = true;
        }
      }
  
      return true;
    }
  
    // Evento de clic en el tablero
    boardElement.addEventListener('click', (ev) => {
      if (gameOver) return;
  
      const target = ev.target;
      if (!target.classList.contains('square')) return;
  
      const row = +target.dataset.row, col = +target.dataset.col;
  
      if (!selectedSquare) {
        // Seleccionar
        const piece = board[row][col];
        if (piece!=='.' && pieceColor(piece)===currentPlayer) {
          selectedSquare = {r: row, c: col};
          target.classList.add('selected');
        }
      } else {
        // Quitar selección visual
        const squares = boardElement.querySelectorAll('.square');
        squares.forEach(sq => sq.classList.remove('selected'));
  
        // Intentar mover
        tryMove(selectedSquare, {r: row, c: col});
        selectedSquare=null;
  
        // Redibujar tablero
        drawBoard();
      }
    });
  
    // Iniciar
    drawBoard();
  });
  