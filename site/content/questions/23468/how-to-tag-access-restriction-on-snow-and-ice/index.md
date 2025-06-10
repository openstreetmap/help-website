+++
type = "question"
title = "How to tag access restriction on snow and ice"
description = '''We have many footway with a sign „Bei Schnee- und Eisglätte gesperrt“ wich means &quot;access restricted when slippy from snow or ice&quot;. How to tag that?'''
date = "2013-06-17T22:12:00Z"
lastmod = "2021-10-27T00:08:00Z"
weight = 23468
keywords = [ "access", "footpath", "slippy", "footway" ]
aliases = [ "/questions/23468" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag access restriction on snow and ice](/questions/23468/how-to-tag-access-restriction-on-snow-and-ice)

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
<span id="post-23468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23468-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We have many footway with a sign „Bei Schnee- und Eisglätte gesperrt“ wich means "access restricted when slippy from snow or ice". How to tag that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-footpath" rel="tag" title="see questions tagged &#39;footpath&#39;">footpath</span> <span class="post-tag tag-link-slippy" rel="tag" title="see questions tagged &#39;slippy&#39;">slippy</span> <span class="post-tag tag-link-footway" rel="tag" title="see questions tagged &#39;footway&#39;">footway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jun '13, 22:12</strong></p>
<img src="https://secure.gravatar.com/avatar/7ef3a3c25492438c9f0e5a548a36fa07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ogmios&#39;s gravatar image" />
<p><span>Ogmios</span><br />
<span class="score" title="766 reputation points">766</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ogmios has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-23468" class="comments-container">
<span id="23485"></span>
<div id="comment-23485" class="comment">
<div id="post-23485-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The obligatory taginfo link:</p>
<p><a href="http://taginfo.openstreetmap.org/search?q=access%3Aconditional%3Dno%40snow">http://taginfo.openstreetmap.org/search?q=access%3Aconditional%3Dno%40snow</a></p>
</div>
<div id="comment-23485-info" class="comment-info">
<span class="comment-age">(18 Jun '13, 13:53)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23468-form-container" class="comment-form-container">
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

<span id="23480"></span>

<div id="answer-container-23480" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23480-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-23480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ogmios has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming that the "ice" condition has a meaning which is distinct from "snow", the intent of the access conditions thing is to allow you to tag like this (for a logical "OR"):</p>
<pre><code>access=yes
access:conditional=no @ snow; no @ ice</code></pre>
<p>However, neither "@ snow" nor "@ ice" is documented properly, which is problematic. I think from the wording that "@ snow" refers to a road condition.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '13, 12:38</strong></p>
<img src="https://secure.gravatar.com/avatar/b4a99bb74962d3cedff3e6d591847852?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrew%20Chadwick&#39;s gravatar image" />
<p><span>Andrew Chadwick</span><br />
<span class="score" title="1129 reputation points"><span>1.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrew Chadwick has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-23480" class="comments-container">
<span id="23481"></span>
<div id="comment-23481" class="comment">
<div id="post-23481-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(If they're not distinct conditions, just use "access:conditional=no @ snow")</p>
</div>
<div id="comment-23481-info" class="comment-info">
<span class="comment-age">(18 Jun '13, 12:39)</span> <span class="comment-user userinfo">Andrew Chadwick</span>
</div>
</div>
<span id="23487"></span>
<div id="comment-23487" class="comment">
<div id="post-23487-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually <em>snow</em> is mentioned in the conditional restrictions wiki page. Nevertheless this page will never be complete so I guess it is valid to introduce new conditions. Taginfo will help as time goes by.</p>
</div>
<div id="comment-23487-info" class="comment-info">
<span class="comment-age">(18 Jun '13, 13:56)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23480" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23480-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82381"></span>

<div id="answer-container-82381" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82381-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Referring to <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions">https://wiki.openstreetmap.org/wiki/Conditional_restrictions</a> the right way would be</p>
<blockquote>
<p>access:conditional=no @ snow; no @ ice</p>
</blockquote>
<p>Notes:</p>
<ul>
<li><code>:conditional</code> does not allow <code>OR</code>. Using multiple parts instead works just fine.</li>
<li><code>:conditional</code> does not allow <code>NOT</code>. Use a different value: <code>access:conditional=no @ snow; no @ ice; yes @ "special caution"</code></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '21, 00:08</strong></p>
<img src="https://secure.gravatar.com/avatar/0ada3899f3deb5d474ee4ed90ee37e8a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="trapicki&#39;s gravatar image" />
<p><span>trapicki</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="trapicki has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82381" class="comments-container">
&#10;</div>
<div id="comment-tools-82381" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82381-form-container" class="comment-form-container">
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

