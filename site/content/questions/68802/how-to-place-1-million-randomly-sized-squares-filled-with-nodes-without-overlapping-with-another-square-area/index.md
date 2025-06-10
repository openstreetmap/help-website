+++
type = "question"
title = "[closed] How to place 1 million randomly sized, squares filled with nodes without overlapping with another square area?"
description = '''Basically I want to place, non-overlapping randomly sized, square filled with nodes (a growing square spiral), which are added real-time so I can&#x27;t predict how large a square will get, but the maximum square can hold 100 million (10,000 X 10,000) nodes. All nodes belonging inside this square have th...'''
date = "2019-04-15T23:29:00Z"
lastmod = "2019-04-18T21:11:00Z"
weight = 68802
keywords = [ "javascript" ]
aliases = [ "/questions/68802" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How to place 1 million randomly sized, squares filled with nodes without overlapping with another square area?](/questions/68802/how-to-place-1-million-randomly-sized-squares-filled-with-nodes-without-overlapping-with-another-square-area)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68802-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-68802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Basically I want to place, non-overlapping randomly sized, square filled with nodes (a growing square spiral), which are added real-time so I can't predict how large a square will get, but the maximum square can hold 100 million (10,000 X 10,000) nodes. All nodes belonging inside this square have the same link to the original starting node.</p>
<p>Right now I generate these random start coordinates where the square spiral begins to grow, to minimize overlaps with another growing bounding box arising from a totally new random seed coordinates that by some chance, happens to be close enough that the two boxes end up overlapping each other.</p>
<pre><code>var memdb = require(&#39;memdb&#39;)
var Osm = require(&#39;kappa-osm&#39;)
&#10;var osm = Osm({
  core: kappa(&#39;./db&#39;, { valueEncoding: &#39;json&#39; }),
  index: memdb(),
  storage: function (name, cb) { cb(null, ram()) }
})
var i = 0;
var startingPoints = [];
while (i &lt; 1000000){
  var node = {
   type: &#39;node&#39;,
   lat: (Math.random()*180-95).toFixed(7).toString(),
   lon: (Math.random()*360-180).toFixed(7).toString(),
   tags: { feature: &#39;randomID&#39;, level: &#39;0&#39; },
   links: [&quot;25235235@0&quot;]
   changeset: &#39;&#39;
  }
   osm.create(node, function (err, node) {
    if (err) return console.error(err)
      startingPoints.push(node);
    })
 ++i;
}
&#10;
startingPoints.forEach(startCoordinates =&gt;{
   fillSquareWithRandomLinkedNodes(startCoordinates, random(2, 1,000,000,000));
})</code></pre>
<p>basically <code>fillSquareWithRandomLinkedNodes</code> generates a random square area size and fills it completely with nodes all linked to provided <code>startCoordinates</code>.</p>
<p>I'm afraid that if I generate 1,000,000 random start coordinates and grow a square spiral square for each coordinate with varying square area size, starting at each point in the clockwise direction, there will be overlapping square shaped spiral of nodes eventually.</p>
<p>I do have some upper limits as to the maximum area of each square spiral, it should be able to store 100 million nodes.</p>
<p>I am assuming there will be issues when more than one node occupies the same longitude and latitude. I've thought about using the <code>level</code> tag but that seems complicated.</p>
<p>or is this overkill, will the overlaps somehow be automatically be handled when querying for all nodes within?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '19, 23:29</strong></p>
<img src="https://secure.gravatar.com/avatar/55d4ebd4a3adf8bf913b5d58b59028c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="studentofosm&#39;s gravatar image" />
<p><span>studentofosm</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="studentofosm has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>16 Apr '19, 08:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-68802" class="comments-container">
<span id="68803"></span>
<div id="comment-68803" class="comment">
<div id="post-68803-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How is this related to OSM? Looks like your question fits better on <a href="http://stackoverflow.com/">http://stackoverflow.com/</a> or <a href="http://gis.stackexchange.com/.">http://gis.stackexchange.com/.</a> Oh, it is already there: <a href="https://stackoverflow.com/questions/55697912/osm-how-to-place-1-million-randomly-sized-squares-filled-with-nodes-without-ov">https://stackoverflow.com/questions/55697912/osm-how-to-place-1-million-randomly-sized-squares-filled-with-nodes-without-ov</a></p>
</div>
<div id="comment-68803-info" class="comment-info">
<span class="comment-age">(16 Apr '19, 07:40)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="68841"></span>
<div id="comment-68841" class="comment">
<div id="post-68841-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I posted it there for visibility but they link it to this thread which effectively kills my question</p>
</div>
<div id="comment-68841-info" class="comment-info">
<span class="comment-age">(18 Apr '19, 21:11)</span> <span class="comment-user userinfo">studentofosm</span>
</div>
</div>
</div>
<div id="comment-tools-68802" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68802-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Frederik Ramm 16 Apr '19, 08:34

</div>

</div>

</div>

