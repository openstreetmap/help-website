+++
type = "question"
title = "Why do some road names contain semicolons (;) ?"
description = '''Why do some road names contain semicolons ?'''
date = "2010-07-16T17:38:00Z"
lastmod = "2010-07-16T19:53:00Z"
weight = 268
keywords = [ "ways", "tagging" ]
aliases = [ "/questions/268" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why do some road names contain semicolons (;) ?](/questions/268/why-do-some-road-names-contain-semicolons)

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
<span id="post-268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-268-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Why do some road names contain <a href="http://www.openstreetmap.org/?lat=51.104317&amp;lon=3.999096&amp;zoom=18&amp;layers=B000FTFTT">semicolons</a> ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '10, 17:38</strong></p>
<img src="https://secure.gravatar.com/avatar/d25927545eb18b4d577280081df5ce6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nic%20Roets&#39;s gravatar image" />
<p><span>Nic Roets</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nic Roets has one accepted answer">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Sep '10, 22:08</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-268" class="comments-container">
&#10;</div>
<div id="comment-tools-268" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-268-form-container" class="comment-form-container">
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

<span id="273"></span>

<div id="answer-container-273" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-273-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-273-score" class="post-score" title="current number of votes">
10
</div>
<span id="post-273-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Without looking at the history of your example, it's likely that someone joined two segments of the road that had different name tags. So <code>name=Main Street</code> joined to <code>name=High Street</code>, in JOSM and Potlatch, becomes <code>name=Main Street; High Street</code>. This should be corrected by splitting the way and tagging the part named Main Street as Main Street and the part named High Street as High Street.</p>
<p>It gets more complicated when a segment of road has more than one name. Here you'll want to place one name (usually the most common on-the-ground) in the name field, and use <span>alt_name</span> and other tags for other names, for instance <code>name=Sixth Avenue</code> <code>official_name=Avenue of the Americas</code>.</p>
<p>I've also seen the route number included in the name, like <code>name=Main Street; United States Highway 66</code>. This would be better handled as <code>name=Main Street ref=US 66</code>.</p>
<p>And, just maybe, there are a few actual road names with semicolons.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '10, 19:53</strong></p>
<img src="https://secure.gravatar.com/avatar/0c334b9f230e39c1e73a2b0322a23fb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NE2&#39;s gravatar image" />
<p><span>NE2</span><br />
<span class="score" title="1359 reputation points"><span>1.4k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NE2 has one accepted answer">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Sep '10, 22:10</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-273" class="comments-container">
&#10;</div>
<div id="comment-tools-273" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-273-form-container" class="comment-form-container">
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

