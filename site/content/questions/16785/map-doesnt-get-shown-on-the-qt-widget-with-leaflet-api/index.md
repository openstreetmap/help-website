+++
type = "question"
title = "[closed] Map doesn&#x27;t get &quot;shown&quot; on the Qt widget with Leaflet API"
description = '''See the snapshot below. I am able to click markers on this map and I can also display the lat longs on it.  But I just can&#x27;t see the map!   The code is here. This function gets called first. function displayMapAndClick () {  map = L.map (&#x27;map&#x27;,   {  dragging: true,  }).setView([51.505, -0.09], 13, t...'''
date = "2012-10-10T06:20:00Z"
lastmod = "2012-10-10T08:23:00Z"
weight = 16785
keywords = [ "openstreetmap", "leaflet", "qt" ]
aliases = [ "/questions/16785" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] Map doesn't get "shown" on the Qt widget with Leaflet API](/questions/16785/map-doesnt-get-shown-on-the-qt-widget-with-leaflet-api)

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
<span id="post-16785-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16785-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16785-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>See the snapshot below. I am able to click markers on this map and I can also display the lat longs on it.</p>
<p>But I just can't <strong><em>see</em></strong> the map!</p>
<p><img src="/upfiles/os_4.png" alt="alt text" /></p>
<hr />
<p><strong>The code is here. This function gets called</strong> first<strong>.</strong></p>
<pre><code>function displayMapAndClick ()
{
    map = L.map (&#39;map&#39;, 
    {
        dragging: true,
    }).setView([51.505, -0.09], 13, true);
&#10;    L.tileLayer(&#39;http://{s}.tile.cloudmade.com/API-key/997/256/{z}/{x}/{y}.png&#39;, 
    {
        attribution: &#39;Map data &amp;copy; &lt;a href=&quot;http://openstreetmap.org&quot;&gt;OpenStreetMap&lt;/a&gt; contributors, &lt;a href=&quot;http://creativecommons.org/licenses/by-sa/2.0/&quot;&gt;CC-BY-SA&lt;/a&gt;, Imagery © &lt;a href=&quot;http://cloudmade.com&quot;&gt;CloudMade&lt;/a&gt;&#39;,
        maxZoom: 13,
        styleId: 997
    }).addTo(map);
&#10;    selectCenterPoint ();
}</code></pre>
<hr />
<p><strong>The Qt's code which accesses the open street map url is:</strong></p>
<pre><code>void Map::geoCode (QString local)
{
    clearCoordinates ();
&#10;    QString url = &quot;http://openstreetmap.org/&quot;;
    manager-&gt;get (QNetworkRequest (QUrl (url)));
    ++pendingRequests;
}</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-qt" rel="tag" title="see questions tagged &#39;qt&#39;">qt</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Oct '12, 06:20</strong></p>
<img src="https://secure.gravatar.com/avatar/0848a0cab04ba90c16abc4c8f32904d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anisha%20Kaul&#39;s gravatar image" />
<p><span>Anisha Kaul</span><br />
<span class="score" title="29 reputation points">29</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anisha Kaul has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>15 Apr '13, 23:26</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-16785" class="comments-container">
&#10;</div>
<div id="comment-tools-16785" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16785-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered, right answer was accepted" by Jonathan Bennett 15 Apr '13, 23:26

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16787"></span>

<div id="answer-container-16787" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16787-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16787-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-16787-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Anisha Kaul has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Did you replace <em>API-key</em> in the CloudMade tile URL?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '12, 06:41</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-16787" class="comments-container">
<span id="16788"></span>
<div id="comment-16788" class="comment">
<div id="post-16788-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@scai</span> No, do I have to replace it? Sorry, didn't know about it. From where do we get a separate key?</p>
</div>
<div id="comment-16788-info" class="comment-info">
<span class="comment-age">(10 Oct '12, 06:44)</span> <span class="comment-user userinfo">Anisha Kaul</span>
</div>
</div>
<span id="16790"></span>
<div id="comment-16790" class="comment">
<div id="post-16790-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span>@Anisha</span>-Kaul Yes I think so, seems like you just have to register to get a free API key.</p>
</div>
<div id="comment-16790-info" class="comment-info">
<span class="comment-age">(10 Oct '12, 07:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="16791"></span>
<div id="comment-16791" class="comment">
<div id="post-16791-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@scai</span> Ok, I''l try that and folow up soon. :)</p>
</div>
<div id="comment-16791-info" class="comment-info">
<span class="comment-age">(10 Oct '12, 07:31)</span> <span class="comment-user userinfo">Anisha Kaul</span>
</div>
</div>
<span id="16792"></span>
<div id="comment-16792" class="comment">
<div id="post-16792-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@scai</span> I registered at <em>CloudMade</em>, and got the key. but this didn't help in anything. The map isn't yet displayed.</p>
</div>
<div id="comment-16792-info" class="comment-info">
<span class="comment-age">(10 Oct '12, 08:07)</span> <span class="comment-user userinfo">Anisha Kaul</span>
</div>
</div>
<span id="16793"></span>
<div id="comment-16793" class="comment not_top_scorer">
<div id="post-16793-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you use a tool like Wireshark to see which tile URL it tries to open and to check whether this URL is valid?</p>
</div>
<div id="comment-16793-info" class="comment-info">
<span class="comment-age">(10 Oct '12, 08:12)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="16794"></span>
<div id="comment-16794" class="comment">
<div id="post-16794-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span>@scai</span> I again restarted the application, and this time the map did get displayed. The key has done the trick I think. <strong>Please put your comment as an answer and I'll select it.</strong> Thanks,.</p>
</div>
<div id="comment-16794-info" class="comment-info">
<span class="comment-age">(10 Oct '12, 08:23)</span> <span class="comment-user userinfo">Anisha Kaul</span>
</div>
</div>
</div>
<div id="comment-tools-16787" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-16787-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

