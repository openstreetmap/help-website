+++
type = "question"
title = "API howto please"
description = '''I have got the book on OSM by Ramm and Topf. And I read the Wiki about the API 0.6 and followed the link to http://en.wikipedia.org/wiki/Representational_State_Transfer. I have managed to try all the examples which can be done with a simple URL. Works fine. But somehow something is missing. How can ...'''
date = "2010-10-31T12:52:00Z"
lastmod = "2010-11-01T19:28:00Z"
weight = 1377
keywords = [ "wiki", "api", "methods" ]
aliases = [ "/questions/1377" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [API howto please](/questions/1377/api-howto-please)

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
<span id="post-1377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1377-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have got the book on OSM by Ramm and Topf. And I read the Wiki about the API 0.6 and followed the link to <a href="http://en.wikipedia.org/wiki/Representational_State_Transfer">http://en.wikipedia.org/wiki/Representational_State_Transfer</a>.</p>
<p>I have managed to try all the examples which can be done with a simple URL. Works fine.</p>
<p>But somehow something is missing. How can I actually use the methods like in a session? There is an illustration in the Wikipedia (a screenshot) showing the use of telnet. I have not found documentation for the OSM API for telnet. Would that be an acceptable way to use the API? What exact URL and what port? 23 or 80?</p>
<p>Could somebody give some practical example for a "dialog" with the API please.</p>
<p>Working on a tiny town in West Africa. So far all is still visible on a single screen in JOSM. But things are getting more complex and soon I could benefit from a structured use of the API.</p>
<p>thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wiki" rel="tag" title="see questions tagged &#39;wiki&#39;">wiki</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-methods" rel="tag" title="see questions tagged &#39;methods&#39;">methods</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '10, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/30c20cb2762636db14c36322853ed87d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Screentoosmall&#39;s gravatar image" />
<p><span>Screentoosmall</span><br />
<span class="score" title="66 reputation points">66</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Screentoosmall has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1377" class="comments-container">
&#10;</div>
<div id="comment-tools-1377" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1377-form-container" class="comment-form-container">
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

<span id="1380"></span>

<div id="answer-container-1380" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1380-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-1380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Screentoosmall has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The API is meant to be used by editing software, such as JOSM, Potlatch 2 or Merkaartor. It is not, in itself, user-facing. You are not expected to communicate directly with it yourself; rather, you use editing software to do that for you. The P in API stands for "Programming" and it means exactly that.</p>
<p>There is no Telnet interface to the API nor will there be. You could use command-line tools and text editors to communicate manually with the API if you really wanted, but it's very, very hard work.</p>
<p>Standard practice for making "programmatic" changes is to download the data using editor software (usually JOSM, which appeals to this sort of tech-savvy audience); save it as an .osm file; munge it somehow using your scripting language of choice; then re-upload using JOSM. However, this sort of editing can really hack people off if done badly, so exercise great caution if you're doing it in an area where other people are mapping.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '10, 19:15</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Nov '10, 07:53</strong> </span></p>
</div>
</div>
<div id="comments-container-1380" class="comments-container">
<span id="1402"></span>
<div id="comment-1402" class="comment">
<div id="post-1402-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you very much. I was mainly after information as in filtered searches for missing tags etc - No worries, I will not mess with scripting anytime soon, neither via API nor via JOSM.</p>
<p>The technical data is all there in the wiki, but with your few sentences, it is now all put into perspective for me. Thanks</p>
</div>
<div id="comment-1402-info" class="comment-info">
<span class="comment-age">(01 Nov '10, 19:28)</span> <span class="comment-user userinfo">Screentoosmall</span>
</div>
</div>
</div>
<div id="comment-tools-1380" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1380-form-container" class="comment-form-container">
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

