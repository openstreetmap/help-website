+++
type = "question"
title = "Osmium - CyclOSM data"
description = '''Hi all, I am using Osmium to extract data from a europe_latest.pbf file. I am trying to find the correct request in order to map the International, National, Regional and Local bike routes as presented on the CyclOSM website: https://www.cyclosm.org/#map=5/47.730/17.830/cyclosm_live I have not figur...'''
date = "2021-06-03T16:08:00Z"
lastmod = "2021-06-07T10:11:00Z"
weight = 80402
keywords = [ "osmium", "europe", "cyclosm", "cycling", "request" ]
aliases = [ "/questions/80402" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Osmium - CyclOSM data](/questions/80402/osmium-cyclosm-data)

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
<span id="post-80402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80402-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I am using Osmium to extract data from a europe_latest.pbf file.</p>
<p>I am trying to find the correct request in order to map the International, National, Regional and Local bike routes as presented on the CyclOSM website: <a href="https://www.cyclosm.org/#map=5/47.730/17.830/cyclosm_live">https://www.cyclosm.org/#map=5/47.730/17.830/cyclosm_live</a></p>
<p>I have not figured it out yet. I tried requests such as <code>osmium tags-filter data/_pbf/europe-latest.osm.pbf wr/route=bicycle wr/network=icn -o data/_osm/europe_cycleways_int.osm</code> but the export file is very huge. It seems it is not filtered as the multitagging would suggest.</p>
<p>Have someone already tried working on cycling routes with Osmium?</p>
<p>Thank you for your time.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-europe" rel="tag" title="see questions tagged &#39;europe&#39;">europe</span> <span class="post-tag tag-link-cyclosm" rel="tag" title="see questions tagged &#39;cyclosm&#39;">cyclosm</span> <span class="post-tag tag-link-cycling" rel="tag" title="see questions tagged &#39;cycling&#39;">cycling</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '21, 16:08</strong></p>
<img src="https://secure.gravatar.com/avatar/2938dda98f86560b48f2afbdcce51fb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lina%20Kortobi&#39;s gravatar image" />
<p><span>Lina Kortobi</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lina Kortobi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80402" class="comments-container">
<span id="80416"></span>
<div id="comment-80416" class="comment">
<div id="post-80416-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Not sure what you mean with "very huge". When you ask for the all bicycle routes you'll get lots of roads over which those routes go, so that is quite a bit of data. So that seems normal. Not sure also what you mean with "multitagging". It seems you need to familiarize yourself a bit more with the OSM data model. Have a look at the -R and -t options, maybe one or the other is what you need.</p>
</div>
<div id="comment-80416-info" class="comment-info">
<span class="comment-age">(04 Jun '21, 09:36)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="80417"></span>
<div id="comment-80417" class="comment">
<div id="post-80417-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>By multitagging I meant using the osmium tool to filter the request. In the example above, when I type wr/route=bicycle wr/network=icn, I want it to understand there is an 'and' between the tags - bicycle routes and international networks which would export only the international bicycle routes. However, I end up with all of them, and some of them are not even bicycle routes in my extract.</p>
</div>
<div id="comment-80417-info" class="comment-info">
<span class="comment-age">(04 Jun '21, 09:43)</span> <span class="comment-user userinfo">Lina Kortobi</span>
</div>
</div>
</div>
<div id="comment-tools-80402" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80402-form-container" class="comment-form-container">
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

<span id="80434"></span>

<div id="answer-container-80434" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80434-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems to me that osmium tags-filter do OR not AND. You can however do what you want in two passes, which would be efficient if you want international, national and regional routes in separate files.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '21, 18:17</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-80434" class="comments-container">
<span id="80444"></span>
<div id="comment-80444" class="comment">
<div id="post-80444-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your help! What would exactly be doing it in two passes?</p>
</div>
<div id="comment-80444-info" class="comment-info">
<span class="comment-age">(07 Jun '21, 10:05)</span> <span class="comment-user userinfo">Lina Kortobi</span>
</div>
</div>
<span id="80445"></span>
<div id="comment-80445" class="comment">
<div id="post-80445-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Create a first file containing all route=bicycle, then filter this file with network=icn.</p>
</div>
<div id="comment-80445-info" class="comment-info">
<span class="comment-age">(07 Jun '21, 10:11)</span> <span class="comment-user userinfo">yvecai</span>
</div>
</div>
</div>
<div id="comment-tools-80434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80434-form-container" class="comment-form-container">
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

