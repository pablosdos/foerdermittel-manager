export function filterPrograms (filter, programs) {
  const log = true
  const logCounter = false
  if (logCounter) {
    console.log('ANZAHL DER FÖRDERMITTEL (filters.js)')
    console.log(Object.keys(programs[0]).length)
  }
  if (log) {
    console.log('DATENSATZ, SO WIE ER ALS ANTWORT KOMMT.')
    console.log(programs)
  }
  // filtered WIRD ERZEUGT, DAMIT DIE FILTER DARAUF ANGEWANDT WERDEN KÖNNEN. DATENSTRUKTUR MUSS DAZU NÄMLICH GEÄNDERT WERDEN.
  let filteredList = [...programs][0]
  filteredList = Object.entries(filteredList)
  let filtered = filteredList

  // Filter region
  if (filter.region !== 'Alle') {
    if (log) {
      console.log('DATENSATZ, WELCHER FILTERBAR GEMACHT WURDE. IN REGION')
      console.log(filtered)
    }
    filtered = filteredList.filter(program => program[1].region.toLowerCase() === filter.region.toLowerCase())
  }

  // Filter theme
  if (filter.theme !== 'Alle') {
    if (log) {
      console.log('DATENSATZ, WELCHER FILTERBAR GEMACHT WURDE. IN THEMEN')
      console.log(filtered)
    }
    filtered = filtered.filter(function (program) {
      let temp = []
      for (let i = 0; i < program[1].area.length; i++) {
        temp = program[1].area[i].toLowerCase() === filter.theme.toLowerCase()
        // falls es temp schon gibt dann überspringen
        if (temp) {
          return temp
        }
        if (log) {
          console.log('i:' + i)
        }
      }
      if (log) {
        console.log('temp')
        console.log(temp)
      }
      return temp
    }
    )
    if (log) {
      console.log('DATENSATZ, WELCHER FILTERBAR GEMACHT WURDE. NACH THEMEN')
      console.log(filtered)
    }
  }

  // Filter type
  if (filter.type !== 'Alle') {
    if (log) {
      console.log('DATENSATZ, WELCHER FILTERBAR GEMACHT WURDE. IN TYPES')
      console.log(filtered)
    }
    filtered = filtered.filter(program => program[1].type.toLowerCase() === filter.type.toLowerCase())
  }

  // console.log(filteredList)
  if (log) {
    console.log('SO SIEHT ARRAY VOR SUCHE AUS')
    console.log(filtered)
  }
  // Search | Stellt die gefilterte Liste zusammen
  if (filter.search !== '') {
    if (log) {
      console.log('es wird gesucht')
    }
    const searchList = []
    const searchTerm = filter.search.toLowerCase()
    if (log) {
      console.log('SUCHWORT AUS STATE')
      console.log(searchTerm)
    }
    for (let i = 0; i < filtered.length; i++) {
      if (filtered[i][1].name !== null && filtered[i][1].name.toLowerCase().includes(searchTerm)) {
        if (log) {
          console.log('stimmt überein')
        }
        searchList.push(filtered[i])
      }
    }
    filtered = searchList
  }

  // LOOP DURCH ARRAY, UM NEUES OBJEKT ZUSAMMENZUSTELLEN.
  /* eslint-disable */
  var object = new Object()
  const x = filtered.length
  for (var i=0; i<x; i++) {
    object[i] = filtered[i][1]
  };
  //  OBJEKT WIRD IN EIN ARRAY VERSCHOBEN.
  /* eslint-enable */
  // filtered = object
  // filteredList = filtered
  let array = [object]
  filteredList = array
  object = null
  array = null

  // console.log(filteredList)
  if (log) {
    console.log('DATENSATZ, AUFGEARBEITET FÜR KOMPONENTEN.')
    console.log(filteredList)
  }

  return filteredList
}

export function orderPrograms (order, programs) {
  const orderedList = [...programs]
  orderedList.sort(function (a, b) {
    const nameA = a[order] ? a[order].toLowerCase() : 'zzz'
    const nameB = b[order] ? b[order].toLowerCase() : 'zzz'
    return nameA < nameB ? -1 : 1
  })
  return orderedList
}

export function sleep (ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms)
  })
}
