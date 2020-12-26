/**
 * @param {string} sequence_text
 */


// https://medium.com/javascript-in-plain-english/how-to-deep-copy-objects-and-arrays-in-javascript-7c911359b089
const deepCopyFunction = (inObject) => {
  let outObject, value, key

  if (typeof inObject !== "object" || inObject === null) {
    return inObject // Return the value if inObject is not an object
  }

  // Create an array or object to hold the values
  outObject = Array.isArray(inObject) ? [] : {}

  for (key in inObject) {
    value = inObject[key]

    // Recursively (deep) copy for nested objects, including arrays
    outObject[key] = deepCopyFunction(value)
  }

  return outObject
}

function print_code_matrix(code_matrix) {
  for (column = 0; column < 6; column++) {
    for (row = 0; row < 6; row++) {
      var id = 's' + column.toString() + row.toString()
      var value = ((code_matrix[column][row] != "") ? code_matrix[column][row] : "--")
      document.getElementById(id).innerHTML = value
    }
  }
}

function read_code_matrix() {
  // Read values
  e00 = document.getElementById('e00').value
  e10 = document.getElementById('e10').value
  e20 = document.getElementById('e20').value
  e30 = document.getElementById('e30').value
  e40 = document.getElementById('e40').value
  e50 = document.getElementById('e50').value

  e01 = document.getElementById('e01').value
  e11 = document.getElementById('e11').value
  e21 = document.getElementById('e21').value
  e31 = document.getElementById('e31').value
  e41 = document.getElementById('e41').value
  e51 = document.getElementById('e51').value

  e02 = document.getElementById('e02').value
  e12 = document.getElementById('e12').value
  e22 = document.getElementById('e22').value
  e32 = document.getElementById('e32').value
  e42 = document.getElementById('e42').value
  e52 = document.getElementById('e52').value

  e03 = document.getElementById('e03').value
  e13 = document.getElementById('e13').value
  e23 = document.getElementById('e23').value
  e33 = document.getElementById('e33').value
  e43 = document.getElementById('e43').value
  e53 = document.getElementById('e53').value

  e04 = document.getElementById('e04').value
  e14 = document.getElementById('e14').value
  e24 = document.getElementById('e24').value
  e34 = document.getElementById('e34').value
  e44 = document.getElementById('e44').value
  e54 = document.getElementById('e54').value

  e05 = document.getElementById('e05').value
  e15 = document.getElementById('e15').value
  e25 = document.getElementById('e25').value
  e35 = document.getElementById('e35').value
  e45 = document.getElementById('e45').value
  e55 = document.getElementById('e55').value

  var code_matrix = [[e00, e01, e02, e03, e04, e05],
  [e10, e11, e12, e13, e14, e15],
  [e20, e21, e22, e23, e24, e25],
  [e30, e31, e32, e33, e34, e35],
  [e40, e41, e42, e43, e44, e45],
  [e50, e51, e52, e53, e54, e55]
  ]

  return code_matrix
}

function text_to_sequence(sequence_text) {
  if (sequence_text.length % 2 != 0) alert("Error processing sequence!")

  var sequence = []
  while (sequence_text.length != 0) {
    sequence.push(sequence_text.substring(0, 2))
    sequence_text = sequence_text.substring(2, sequence_text.length)
  }
  return sequence
}

function find_best_sequence(ram) {
  var datamine1 = text_to_sequence(document.getElementById('d1').value)
  var datamine2 = text_to_sequence(document.getElementById('d2').value)
  var datamine3 = text_to_sequence(document.getElementById('d3').value)

  // var ram = parseInt(document.getElementById('ram').value)

  var sequences = []

  console.log(datamine1)
  console.log(datamine2)
  console.log(datamine3)

  //Check possible links between sequences
  _1_2 = datamine1[datamine1.length - 1] == datamine2[0]
  _1_3 = datamine1[datamine1.length - 1] == datamine3[0]
  _2_1 = datamine2[datamine2.length - 1] == datamine1[0]
  _2_3 = datamine2[datamine2.length - 1] == datamine3[0]
  _3_1 = datamine3[datamine3.length - 1] == datamine1[0]
  _3_2 = datamine3[datamine3.length - 1] == datamine2[0]

  if (ram >= datamine3.length) {
    console.log("RAM sufficient for Datamine 3")

    if (ram >= (datamine3.length + datamine2.length + datamine1.length - 2)) {
      console.log("RAM sufficient for combining all three sequences")

      // 1_2_3
      if (_1_2 && _2_3) {
        console.log("Sequence D1-D2-D3 possible: ")
        var seq = datamine1.concat(datamine2.slice(1, datamine2.length)).concat(datamine3.slice(1, datamine3.length))
        console.log(seq)
        sequences.push(seq)
      }

      // 1_3_2
      if (_1_3 && _3_2) {
        console.log("Sequence D1-D3-D2 possible: ")
        var seq = datamine1.concat(datamine3.slice(1, datamine3.length)).concat(datamine2.slice(1, datamine2.length))
        console.log(seq)
        sequences.push(seq)
      }

      // 2_1_3
      if (_2_1 && _1_3) {
        console.log("Sequence D2-D1-D3 possible: ")
        var seq = datamine2.concat(datamine1.slice(1, datamine1.length)).concat(datamine3.slice(1, datamine3.length))
        console.log(seq)
        sequences.push(seq)
      }

      // 2_3_1
      if (_2_3 && _3_1) {
        console.log("Sequence D2-D3-D1 possible: ")
        var seq = datamine2.concat(datamine3.slice(1, datamine3.length)).concat(datamine1.slice(1, datamine1.length))
        console.log(seq)
        sequences.push(seq)
      }

      // 3_1_2
      if (_3_1 && _1_2) {
        console.log("Sequence D3-D1-D2 possible: ")
        var seq = datamine3.concat(datamine1.slice(1, datamine1.length)).concat(datamine2.slice(1, datamine2.length))
        console.log(seq)
        sequences.push(seq)
      }

      // 3_2_1
      if (_3_2 && _2_1) {
        console.log("Sequence D3-D2-D1 possible: ")
        var seq = datamine3.concat(datamine2.slice(1, datamine2.length)).concat(datamine1.slice(1, datamine1.length))
        console.log(seq)
        sequences.push(seq)
      }
    }

    if (ram >= (datamine3.length + datamine2.length - 1)) {
      console.log("RAM sufficient for combining Datamine_v3 with Datamine_v2")

      // 2_3
      if (_2_3) {
        console.log("Sequence D2-D3 possible: ")
        var seq = datamine2.concat(datamine3.slice(1, datamine3.length))
        console.log(seq)
        sequences.push(seq)
      }

      // 3_2
      if (_3_2) {
        console.log("Sequence D3-D2 possible: ")
        var seq = datamine3.concat(datamine2.slice(1, datamine2.length))
        console.log(seq)
        sequences.push(seq)
      }
    }

    if (ram >= (datamine3.length + datamine2.length - 1)) {
      console.log("RAM sufficient for simply adding Datamine_v3 and Datamine_v2")

      console.log("Simple sequence D2-D3 possible: ")
      var seq = datamine2.concat(datamine3)
      console.log(seq)
      sequences.push(seq)

      console.log("Simple sequence D3-D2 possible: ")
      var seq = datamine3.concat(datamine2)
      console.log(seq)
      sequences.push(seq)
    }

    console.log("Only D3: ")
    var seq = datamine3
    console.log(sequences)
    sequences.push(seq)
  }

  console.log("Possible Sequences: ")
  console.log(sequences)

  console.log("Best Sequence: ")
  console.log(sequences[0])

  return sequences
}

function validate_code_matrix(code_matrix) {
  var valid_elements = ['55', '7A', 'BD', '1C', 'E9']

  for (column = 0; column < 6; column++) {
    for (row = 0; row < 6; row++) {
      if (!valid_elements.includes(code_matrix[column][row])) {
        console.log("Code Matrix invalid!")
        return false
      }
    }
  }
  console.log("Code Matrix valid!")
  return true
}

function possible_start_points(code_matrix, value) {
  start_points = []
  for (column = 0; column < 6; column++) {
    for (row = 0; row < 6; row++) {
      if (code_matrix[column][row] == value) {
        start_points.push([column, row])
      }
    }
  }
  console.log("Possible start points for value " + value + " :")
  console.log(start_points)

  return start_points
}

solutions = []

function find_combination_recursive(cm_, ram_left, seq, seq_pos, last_position, vert_horz, remaining_seqence) {
  var cm = deepCopyFunction(cm_)
  var rs = deepCopyFunction(remaining_seqence)

  if (rs.length == 0) {
    //alert("Found Sequence: " + seq_pos)
    var solution = [seq, seq_pos]
    solutions.push(solution)
    return
  }

  if (ram_left < 1) {
    return
  }

  if (vert_horz == 'vert') {
    var column = last_position[0]
    for (var row = 0; row < 6; row++) {
      if (row != last_position[1] && cm[column][row] == rs[0]) {
        var hex_val = cm[column][row]
        cm[column][row] = '--'
        find_combination_recursive(cm, ram_left - 1, seq + hex_val, seq_pos + column.toString() + row.toString(), [column, row], 'horz', rs.slice(1, rs.length))
      }
    }
    return
  }

  else if (vert_horz == 'horz') {
    var row = last_position[1]
    for (var column = 0; column < 6; column++) {
      if (column != last_position[0] && cm[column][row] == rs[0]) {
        var hex_val = cm[column][row]
        cm[column][row] = '--'
        find_combination_recursive(cm, ram_left - 1, seq + hex_val, seq_pos + column.toString() + row.toString(), [column, row], 'vert', rs.slice(1, rs.length))
      }
    }
  }
}

function find_combination(code_matrix, ram, start_point, sequence) {

  console.log("Try to find a combination for sequence " + sequence + " with start point " + start_point)

  var cm = deepCopyFunction(code_matrix)

  var hex_val = sequence[0]
  var column = start_point[0]
  var row = start_point[1]

  if (start_point[1] == 0) {
    // Start in first row
    cm[column][row] = '--'
    find_combination_recursive(cm, ram - 1, hex_val, column.toString() + row.toString(), [column, row], 'vert', sequence.slice(1, sequence.length))
  }
  else {
    // Reach first element from first row
    var seq = cm[column][0] + cm[column][row]
    var seq_pos = column.toString() + '0' + column.toString() + row.toString()
    cm[column][0] = '--'
    cm[column][row] = '--'
    find_combination_recursive(cm, ram - 2, seq, seq_pos, [column, row], 'horz', sequence.slice(1, sequence.length))
  }
}

function solve_seq(code_matrix, seq, ram) {
  console.log("Called solve_seq with ram " + ram + " and sequence " + seq)

  console.log("Validate Code Matrix: ")
  var valid = validate_code_matrix(code_matrix)
  if (!valid) return -1

  var start_points = possible_start_points(code_matrix, seq[0])

  if (!start_points) return

  for (var sp_index = 0; sp_index < start_points.length; sp_index++) {
    find_combination(code_matrix, ram, start_points[sp_index], seq)
  }

  console.log("Found " + solutions.length + " solutions in total")
  return solutions
}

function print_solution(solution_seq) {
  var values = text_to_sequence(solution_seq[0])
  var steps = text_to_sequence(solution_seq[1])

  console.log("Values: " + values)
  console.log("Steps: " + steps)
  console.log("steps.length = " + steps.length)

  var solution_code_matrix = [['--', '--', '--', '--', '--', '--'], ['--', '--', '--', '--', '--', '--'], ['--', '--', '--', '--', '--', '--'],
  ['--', '--', '--', '--', '--', '--'], ['--', '--', '--', '--', '--', '--'], ['--', '--', '--', '--', '--', '--']]

  document.getElementById('seq_values').innerHTML = values

  for (var step_index = 0; step_index < steps.length; step_index++) {
    var column = steps[step_index].substring(0, 1)
    var row = steps[step_index].substring(1, 2)

    console.log("" + column + " " + row)

    solution_code_matrix[column][row] = (step_index + 1).toString() + "."
  }

  print_code_matrix(solution_code_matrix)
}


function solve() {
  code_matrix = read_code_matrix()
  var ram = parseInt(document.getElementById('ram').value)
  sequences = find_best_sequence(ram)

  var code_matrix_debug = [['55', '1C', '55', 'BD', '1C', '7A'], ['7A', 'BD', '1C', '55', 'E9', '1C'],
  ['BD', '55', 'BD', '55', '55', '1C'], ['1C', '55', '1C', 'BD', '55', 'BD'],
  ['55', 'E9', '7A', '1C', '1C', '1C'], ['7A', 'BD', '1C', '55', '55', 'BD']]


  while (sequences.length != 0) {
    var code_matrix = read_code_matrix()
    var solutions_for_sequence = solve_seq(code_matrix, sequences[0], ram)
    if (solutions_for_sequence.length > 0) {
      print_solution(solutions_for_sequence[0])
      break
    }
    sequences = sequences.slice(1, sequences.length)
  }
}