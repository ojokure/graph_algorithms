function paginate(array, size) {
  let paginated = [];
  for (let element of array) {
    let child_last = paginated[paginated.length - 1];
    if (!child_last || child_last.length === size) {
      paginated.push([element]);
    } else {
      child_last.push(element);
    }
  }
  return paginated;
}
function fetchItemsToDisplay(
  items,
  sortParameter,
  sortOrder,
  itemsPerPage,
  pageNumber
) {
  items.sort((a, b) => {
    if (sortParameter === 0) {
      let nameA = a[0].toUpperCase();
      let nameB = b[0].toUpperCase();
      if (nameA < nameB) {
        return sortOrder ? 1 : -1;
      }
      if (nameA > nameB) {
        return sortOrder ? -1 : 1;
      }
      return 0;
    } else if (sortParameter === 1) {
      return sortOrder ? b[1] - a[1] : a[1] - b[1];
    } else if (sortParameter === 2) {
      return sortOrder ? b[2] - a[2] : a[2] - b[2];
    }
  });
  let paginatedItems = paginate(items, itemsPerPage);
  let pages = paginatedItems[pageNumber];
  let itemToDisplay = pages.map((item) => {
    return item[0];
  });

  return itemToDisplay;
}
