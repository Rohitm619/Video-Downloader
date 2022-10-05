let a = document.getElementsByClassName("thumbnail-info-wrapper");
for (let index = 0; index < a.length; index++) {
  let link = a[index].childNodes[1].childNodes[1].href;
  try {
    if (link.includes("https://www.pornhub.com/view_video")) {
      // console.log(link)
      link = link.slice(0, 12) + "ez" + link.slice(12);

      console.log(link);
    }
  } catch (err) {
    continue;
  }
}
