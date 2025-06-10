+++
type = "question"
title = "Tile server system requirements"
description = '''I am thinking of hosting my own tile server for OSM but I am a bit confused about what kind of server I would need. There are several questions about what you need but it never says anything about the load such a server could handle and since the load isn&#x27;t small I am worried it won&#x27;t be enough. Rig...'''
date = "2018-11-13T12:27:00Z"
lastmod = "2018-11-22T08:10:00Z"
weight = 66761
keywords = [ "tileserver" ]
aliases = [ "/questions/66761" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tile server system requirements](/questions/66761/tile-server-system-requirements)

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
<span id="post-66761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66761-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am thinking of hosting my own tile server for OSM but I am a bit confused about what kind of server I would need.</p>
<p>There are several questions about what you need but it never says anything about the load such a server could handle and since the load isn't small I am worried it won't be enough.</p>
<p>Right now we are using Google Maps which has a 100k uses a month and expected is that the average use would need around 40-60 tiles.</p>
<p>Right now we only want to do a single country and I'm mostly worried about RAM and CPU requirements.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Nov '18, 12:27</strong></p>
<img src="https://secure.gravatar.com/avatar/e5766fb2d6293da77814ceff03d0218b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joost67&#39;s gravatar image" />
<p><span>Joost67</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joost67 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66761" class="comments-container">
&#10;</div>
<div id="comment-tools-66761" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66761-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="66770"></span>

<div id="answer-container-66770" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66770-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-66770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are essentially two bits to a tile server** - there's generating the tiles in the first place, and there's serving those tiles out to users. I'll take <a href="https://map.atownsend.org.uk/maps/map/map.html">this</a> as an example since it's a server that I set up. When a user tries to view a tile that does not exist such as <a href="https://map.atownsend.org.uk/hot/13/4096/2665.png">this one</a> a request to render it occurs, and in this case it (and a series of surrounding tiles) took 1.5 seconds to render. This information is in the syslog of the server:</p>
<pre><code>DONE TILE ajt 13 4096-4103 2664-2671 in 1.524 seconds</code></pre>
<p>The next time someone tries to view that tile it doesn't need to be rendered again because it already exists. The existing tile can just be sent out to all the new requests. Only when that tile is quite old, or the rendering system knows that new data from OSM means that that tile is out of date will a new tile be rendered. This means that many of the "100k uses a month of 40-60 tiles" (on average 1 every 2 seconds?) might not cause rendering requests each time - in fact most probably wouldn't - the web server would already have the data to send and no new rendering would take place.</p>
<p>The size of server you'll need for "a single country" depends on the size of the country. Have a look <a href="http://download.geofabrik.de/">at Geofabrik</a> for how big your country is. The server I'm using as an example has the <a href="http://download.geofabrik.de/europe/british-isles.html">British Isles</a> loaded, which is about 1.1Gb of input data. That data comfortably fits on a server (cloud or local) with 4Gb memory and 100Gb disk (until a month ago it was on a CX30 at <a href="https://www.hetzner.com/cloud">Hetzner</a>; it's now moved to a slightly faster CX41 there). Other cloud providers are available and may be better for you depending on all sorts of factors such as where you're located and where you're serving data to. In my case zoom levels up to 12 are pre-rendered; the job runs once a day and each of these tiles are rerendered once every 4 days. Other higher zoom levels (up to 24 in my case) are rendered only as needed. The database size for 1.1Gb of input data is a little over 30Gb currently.</p>
<p>How much oomph your server needs will also depend on:</p>
<ul>
<li>Whether you need to update the data once loaded</li>
<li>How much detail you want to display</li>
<li>How many zoom levels you want to display</li>
<li>What other functions you want the server to support (mine isn't doing routing or geocoding, for example)</li>
</ul>
<p>** for the avoidance of doubt I'm assuming you're talking about similar technology to <a href="https://openstreetmap.org"></a><a href="https://openstreetmap.org">https://openstreetmap.org</a> here. Other technologies are available, but let's keep the answer simple for now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '18, 20:02</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '18, 20:05</strong> </span></p>
</div>
</div>
<div id="comments-container-66770" class="comments-container">
<span id="66888"></span>
<div id="comment-66888" class="comment">
<div id="post-66888-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for you comprehensive reply and I think I have gotten a lot futher. Just out of curiosity can I ask what kind of trafic your server is handling? PS: I am going to do the Netherlands which should be only a little smaller than the British Isles</p>
</div>
<div id="comment-66888-info" class="comment-info">
<span class="comment-age">(22 Nov '18, 08:10)</span> <span class="comment-user userinfo">Joost67</span>
</div>
</div>
</div>
<div id="comment-tools-66770" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66770-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

