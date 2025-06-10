+++
type = "question"
title = "Get OSM map in R"
description = '''Hi,  I am trying to get a map using R and the get_map function. Location.S &amp;lt;- c(3.5, 57.7, 11, 66) Map.South &amp;lt;- get_map(location=Location.S, source=&quot;osm&quot;, color=&quot;bw&quot;, crop=TRUE, language=&quot;en-EN&quot;) ggmap(Map.South) This code worked fine three weeks ago but I now get the following error message: ...'''
date = "2017-01-11T11:57:00Z"
lastmod = "2017-01-12T14:42:00Z"
weight = 53975
keywords = [ "get_map", "r", "error" ]
aliases = [ "/questions/53975" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Get OSM map in R](/questions/53975/get-osm-map-in-r)

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
<span id="post-53975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53975-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am trying to get a map using R and the get_map function.</p>
<p>Location.S &lt;- c(3.5, 57.7, 11, 66)<br />
Map.South &lt;- get_map(location=Location.S, source="osm", color="bw", crop=TRUE, language="en-EN")<br />
ggmap(Map.South)</p>
<p>This code worked fine three weeks ago but I now get the following error message:</p>
<p>Error: map grabbing failed - see details in ?get_openstreetmap. In addition: Warning message: In download.file(url, destfile = destfile, quiet = !messaging, mode = "wb") : cannot open URL 'http://tile.openstreetmap.org/cgi-bin/export?bbox=3.5,57.7,11,66&amp;scale=5000000&amp;format=png': HTTP status was '400 Bad Request'</p>
<p>Any help will be greatly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-get_map" rel="tag" title="see questions tagged &#39;get_map&#39;">get_map</span> <span class="post-tag tag-link-r" rel="tag" title="see questions tagged &#39;r&#39;">r</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jan '17, 11:57</strong></p>
<img src="https://secure.gravatar.com/avatar/684275f0f485a4a473092b1b3de1840f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pierrick0204&#39;s gravatar image" />
<p><span>Pierrick0204</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pierrick0204 has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-53975" class="comments-container">
&#10;</div>
<div id="comment-tools-53975" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53975-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="53979"></span>

<div id="answer-container-53979" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53979-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-53979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This R function seems to run an CGI export call. I'm surprised that it worked at all. An issue has been filed against the github repo requesting that this call not be used: <a href="https://github.com/dkahle/ggmap/issues/117">https://github.com/dkahle/ggmap/issues/117</a>.</p>
<p>The website export call is heavily rate limited. There are numerous examples of queries on this site relating to this issue.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '17, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-53979" class="comments-container">
&#10;</div>
<div id="comment-tools-53979" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53979-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53980"></span>

<div id="answer-container-53980" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53980-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>/cgi-bin/export</code> at openstreetmap.org is not designed for automated requests from scripts! See <a href="https://operations.osmfoundation.org/policies/tiles/">https://operations.osmfoundation.org/policies/tiles/</a> for more details. Quoting this page:</p>
<blockquote>
<p>Calls to /cgi-bin/export may only be triggered by direct end-user action. (For example: “click here to export”.) The export call is an expensive (CPU+RAM) function to run and will frequently reject when server is under high load.</p>
</blockquote>
<p>This means that the <code>get_map()</code> call implementation in R for OSM is broken.</p>
<p>IMHO R should access individual tiles for the specified zoom level instead (without violating the tile usage policy, of course). Afterwards it just has to concatenate these tiles locally. This should be roughly equivalent to a call to <code>/cgi-bin/export</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '17, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-53980" class="comments-container">
<span id="53982"></span>
<div id="comment-53982" class="comment not_top_scorer">
<div id="post-53982-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The call get_openstreetmap() does not semm to work as well. Is there any way I can import the OSM from R since I am plotting data linked to geo coordinates?</p>
</div>
<div id="comment-53982-info" class="comment-info">
<span class="comment-age">(11 Jan '17, 14:00)</span> <span class="comment-user userinfo">Pierrick0204</span>
</div>
</div>
<span id="53983"></span>
<div id="comment-53983" class="comment not_top_scorer">
<div id="post-53983-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can't answer this question since I've never worked with OSM in R.</p>
</div>
<div id="comment-53983-info" class="comment-info">
<span class="comment-age">(11 Jan '17, 14:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="53985"></span>
<div id="comment-53985" class="comment">
<div id="post-53985-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>See the github issue for more on this.</p>
</div>
<div id="comment-53985-info" class="comment-info">
<span class="comment-age">(11 Jan '17, 17:53)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="53992"></span>
<div id="comment-53992" class="comment not_top_scorer">
<div id="post-53992-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi again. If I understand the recent conversation from this post on Github, there is no way I can plot the same OSM map from R? That's really a pity since I used I for a scientific paper from which I have to update the map figure using the same map background as I previously did. Is there any alternative to get through this?</p>
</div>
<div id="comment-53992-info" class="comment-info">
<span class="comment-age">(12 Jan '17, 01:33)</span> <span class="comment-user userinfo">Pierrick0204</span>
</div>
</div>
<span id="53997"></span>
<div id="comment-53997" class="comment">
<div id="post-53997-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can try <a href="http://bigmap.osmz.ru/">BigMap 2</a> to generate an image which you can then embed yourself. Keep in mind that this program will also violate the tile usage policy if used excessively. But for your paper it is probably okay.</p>
</div>
<div id="comment-53997-info" class="comment-info">
<span class="comment-age">(12 Jan '17, 08:19)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="53998"></span>
<div id="comment-53998" class="comment not_top_scorer">
<div id="post-53998-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. Will the generated image contain the geographic coordinates? I need this information to plot my data (aquaculture sites) along the Norwegian coast, based on coordinates.</p>
</div>
<div id="comment-53998-info" class="comment-info">
<span class="comment-age">(12 Jan '17, 08:55)</span> <span class="comment-user userinfo">Pierrick0204</span>
</div>
</div>
<span id="54000"></span>
<div id="comment-54000" class="comment">
<div id="post-54000-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No, the image will just be a regular image. The image generated by <code>/cgi-bin/export</code> also doesn't "contain" coordinates. Instead R knows the bounds of the image and can calculate the coordinates.</p>
</div>
<div id="comment-54000-info" class="comment-info">
<span class="comment-age">(12 Jan '17, 09:58)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="54002"></span>
<div id="comment-54002" class="comment">
<div id="post-54002-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>An alternative would be to use QGIS, the Composer option &amp; Quick Map Services Plugin to create a map from OSM tiles covering the same area. This gives good control over scale and boundaries. I'm not sure exactly how pulling a map into ggplot works though.</p>
</div>
<div id="comment-54002-info" class="comment-info">
<span class="comment-age">(12 Jan '17, 13:26)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="54003"></span>
<div id="comment-54003" class="comment">
<div id="post-54003-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In the meantime, I just figured out the openstreetmap package on R which seem to do more or less the same.</p>
</div>
<div id="comment-54003-info" class="comment-info">
<span class="comment-age">(12 Jan '17, 14:42)</span> <span class="comment-user userinfo">Pierrick0204</span>
</div>
</div>
</div>
<div id="comment-tools-53980" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-53980-form-container" class="comment-form-container">
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

