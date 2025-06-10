+++
type = "question"
title = "XAPI call for all ATMs"
description = '''How can I get all ATMs in a bounding box?  I know how to get &quot;amenity=atm&quot;, but there is also &quot;amenity=bank atm=yes&quot;. OK, I can request for &quot;amenity=&quot; and filter the result for all ATMs. But perhaps &quot;atm=yes&quot; is also used in &quot;aerialway=station&quot; or &quot;tourism=hotel&quot; or whatever. How can I get all ATMs ...'''
date = "2012-04-14T13:36:00Z"
lastmod = "2012-04-14T15:54:00Z"
weight = 12009
keywords = [ "xapi" ]
aliases = [ "/questions/12009" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [XAPI call for all ATMs](/questions/12009/xapi-call-for-all-atms)

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
<span id="post-12009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12009-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I get all ATMs in a bounding box?</p>
<p>I know how to get "amenity=atm", but there is also "amenity=bank atm=yes". OK, I can request for "amenity=<em>" and filter the result for all ATMs. But perhaps "atm=yes" is also used in "aerialway=station" or "tourism=hotel" or whatever. How can I get all ATMs if I don't know in which tags they are hidden? Of course I don't want to download "</em>" (all available data) to reduce traffic and server load.</p>
<p>This is only an example. Actually I am interested of getting any "...=yes" tag, not only ATM.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '12, 13:36</strong></p>
<img src="https://secure.gravatar.com/avatar/218b47dc075c78d7b6edf408fea255f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Plenz&#39;s gravatar image" />
<p><span>Plenz</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Plenz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12009" class="comments-container">
&#10;</div>
<div id="comment-tools-12009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12009-form-container" class="comment-form-container">
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

<span id="12012"></span>

<div id="answer-container-12012" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12012-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You seem to be misunderstanding how tagging works.</p>
<p>An object can have any number of tags (key/value combinations). A bank that also has an ATM would have two tags, <code>amenity=bank</code> and <code>atm=yes</code> (leaving aside the fact that some people use <code>amenity=bank;atm</code> for a moment). So if there is a tag <code>atm=yes</code> then it would not "hide in other tags", it would simply be there in addition to other tags.</p>
<p>An XAPI query for <code>atm=yes</code> would bring up all objects that are thus tagged, including those that also have <code>aerialway=station</code>, those that have <code>tourism=hotel</code> and so on.</p>
<p>The only real problem is in fact the combination of values with a semicolon, so there will be some objects tagged <code>amenity=bank;atm</code> or <code>amenity=fuel;parking</code> making some queries more difficult. But those are exceptions really. Check out <a href="http://taginfo.openstreetmap.org">TagInfo</a> to find out how often certain tags are used, and which combinations are frequent. For example, <a href="http://taginfo.openstreetmap.org/search?q=amenity%3Datm">http://taginfo.openstreetmap.org/search?q=amenity%3Datm</a> tells you that there are about 42k <code>amenity=atm</code>, and <a href="http://taginfo.openstreetmap.org/keys/atm#values">http://taginfo.openstreetmap.org/keys/atm#values</a> lists about 53k instances of <code>atm=yes</code>. The "combinations" tab also tells you that the <code>atm</code> tag is most frequently ised in conjunction with <code>amenity</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '12, 14:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-12012" class="comments-container">
<span id="12015"></span>
<div id="comment-12015" class="comment">
<div id="post-12015-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe I misunderstood tagging, maybe I misunderstood XAPI calls - anyway, I did not know that ".../xapi?*[atm=yes][bbox=..." works. Thanks for that!</p>
<p>But I am afraid I need two XAPI calls if I want to get all ATMs: one call "?node[amenity=atm]" and a second call "?*[atm=yes]". Or is there a way to put both requests into one XAPI call?</p>
</div>
<div id="comment-12015-info" class="comment-info">
<span class="comment-age">(14 Apr '12, 15:31)</span> <span class="comment-user userinfo">Plenz</span>
</div>
</div>
<span id="12016"></span>
<div id="comment-12016" class="comment">
<div id="post-12016-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>To really catch <em>all</em> ATMs you would need even more - you would have to ask for amenity=bank;atm and all those funny other combinations as well. You might consider trying out the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> for more complex queries. Or, you can of course download the whole planet file, place it in a database, and query it to your heart's content...</p>
</div>
<div id="comment-12016-info" class="comment-info">
<span class="comment-age">(14 Apr '12, 15:34)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="12017"></span>
<div id="comment-12017" class="comment">
<div id="post-12017-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Indeed, Overpass API/Language Guide seems to be a page to read.</p>
<p>Unfortunately, there are no wildcard mentioned as for example amenity=*;atm. Will this work or not?</p>
</div>
<div id="comment-12017-info" class="comment-info">
<span class="comment-age">(14 Apr '12, 15:54)</span> <span class="comment-user userinfo">Plenz</span>
</div>
</div>
</div>
<div id="comment-tools-12012" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12012-form-container" class="comment-form-container">
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

