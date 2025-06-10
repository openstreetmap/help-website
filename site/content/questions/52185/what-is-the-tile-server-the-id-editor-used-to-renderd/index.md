+++
type = "question"
title = "What is the tile server the iD editor used to renderd?"
description = '''When i use josm to make an edit on my map, and i have not updata the database that my tile server used to renderd, but when i view the http://192.168.99.128:3000 website, try to use iD editor to make an edit too, i find that the edit page has update the tiles where i edit by josm. So what is the til...'''
date = "2016-09-23T03:41:00Z"
lastmod = "2016-09-23T10:04:00Z"
weight = 52185
keywords = [ "ideditor", "josm", "renderd", "usage", "tileserver" ]
aliases = [ "/questions/52185" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What is the tile server the iD editor used to renderd?](/questions/52185/what-is-the-tile-server-the-id-editor-used-to-renderd)

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
<span id="post-52185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52185-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When i use josm to make an edit on my map, and i have not updata the database that my tile server used to renderd, but when i view the <a href="http://192.168.99.128:3000">http://192.168.99.128:3000</a> website, try to use iD editor to make an edit too, i find that the edit page has update the tiles where i edit by josm. So what is the tile server the iD editor used to renderd? Why the iD editor alaway keep up-to-date even i did not make any configuration on it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '16, 03:41</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Sep '16, 19:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-52185" class="comments-container">
<span id="52189"></span>
<div id="comment-52189" class="comment">
<div id="post-52189-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I assume this question is about your own server? Please could you clarify your setup? What did you install, what did you configure?</p>
</div>
<div id="comment-52189-info" class="comment-info">
<span class="comment-age">(23 Sep '16, 06:25)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="52190"></span>
<div id="comment-52190" class="comment">
<div id="post-52190-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I installed the rails port and built my local tile server, i make my rails port connect to my tile server by change the tiles address in the vendor/assets/openlayers/OpenStreetMap.js and vendor/assets/leaflet/leaflet.osm.js. When i make an edit by the iD editor or josm, the map did not show the changests immediatily, unless i update the gis database and re-rendred the dity tiles, then the changed can be showed on the map. But the iD editor page can alaways show the changests even i did not update the gis database and dity tiles.</p>
</div>
<div id="comment-52190-info" class="comment-info">
<span class="comment-age">(23 Sep '16, 07:14)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
</div>
<div id="comment-tools-52185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52185-form-container" class="comment-form-container">
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

<span id="52191"></span>

<div id="answer-container-52191" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52191-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yuyy has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The iD editor renders the map on its own. There is no tile server involved.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '16, 07:47</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-52191" class="comments-container">
<span id="52192"></span>
<div id="comment-52192" class="comment">
<div id="post-52192-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What is the mean that iD editor renderds the map on its own? How does the iD editor get the map picture that shows to us? Can you explain more detailon it, thanks.</p>
</div>
<div id="comment-52192-info" class="comment-info">
<span class="comment-age">(23 Sep '16, 08:07)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
<span id="52193"></span>
<div id="comment-52193" class="comment">
<div id="post-52193-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Editors (both iD and JOSM) download vector data and render that locally. The default rendering of iD looks quite similar to the default raster tiles on osm.org, which is probably where you got confused (thinking that iD was displaying updated raster tiles when it was actually rendering vector data).</p>
<p>Note that JOSM has extensive render styling capabilities, and that there are lots of different styles for raster tiles too.</p>
</div>
<div id="comment-52193-info" class="comment-info">
<span class="comment-age">(23 Sep '16, 10:03)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="52194"></span>
<div id="comment-52194" class="comment">
<div id="post-52194-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It queries your database for the raw data and just draws it similar to a vector renderer. Editors usually come with their own renderer. In the end this is quite similar to a vector graphics editor like Adobe Illustrator or Inkscape who can also show you immediately all the lines and shapes that you are drawing.</p>
</div>
<div id="comment-52194-info" class="comment-info">
<span class="comment-age">(23 Sep '16, 10:04)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52191" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52191-form-container" class="comment-form-container">
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

