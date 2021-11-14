export function filterPrograms (filter, programs) {
  console.log('DATENSATZ, SO WIE ER ALS ANTWORT KOMMT.')
  console.log(programs)
  // filtered WIRD ERZEUGT, DAMIT DIE FILTER DARAUF ANGEWANDT WERDEN KÖNNEN. DATENSTRUKTUR MUSS DAZU NÄMLICH GEÄNDERT WERDEN.
  let filteredList = [...programs][0]
  filteredList = Object.entries(filteredList)
  let filtered = filteredList

  // Filter region
  if (filter.region !== 'all') {
    console.log('DATENSATZ, WELCHER FILTERBAR GEMACHT WURDE. IN REGION')
    console.log(filtered)
    filtered = filteredList.filter(program => program[1].region.toLowerCase() === filter.region.toLowerCase())
  }

  // Filter theme
  if (filter.theme !== 'all') {
    console.log('DATENSATZ, WELCHER FILTERBAR GEMACHT WURDE. IN THEMEN')
    console.log(filtered)
    filtered = filtered.filter(program => program[1].area[0].toLowerCase() === filter.theme.toLowerCase())
  }

  // Filter type
  if (filter.type !== 'all') {
    console.log('DATENSATZ, WELCHER FILTERBAR GEMACHT WURDE. IN TYPES')
    console.log(filtered)
    filtered = filtered.filter(program => program[1].type.toLowerCase() === filter.type.toLowerCase())
  }

  // console.log(filteredList)
  console.log('SO SIEHT ARRAY VOR SUCHE AUS')
  console.log(filtered)
  // Search | Stellt die gefilterte Liste zusammen
  if (filter.search !== '') {
    console.log('es wird gesucht')
    const searchList = []
    const searchTerm = filter.search.toLowerCase()
    console.log('SUCHWORT AUS STATE')
    console.log(searchTerm)
    for (let i = 0; i < filtered.length; i++) {
      if (filtered[i][1].name !== null && filtered[i][1].name.toLowerCase().includes(searchTerm)) {
        console.log('stimmt überein')
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
  console.log('DATENSATZ, AUFGEARBEITET FÜR KOMPONENTEN.')
  console.log(filteredList)

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
