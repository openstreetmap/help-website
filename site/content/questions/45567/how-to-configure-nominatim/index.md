+++
type = "question"
title = "How to configure Nominatim?"
description = '''Hi, I would like to limit the list of OSM tags my Nominatim server makes use of. I found:  The file phrase_settings.php with a blacklist and a whitelist but the default values don&#x27;t look as if they would be valid. The file partitionedtags.def but it seems to be incomplete. E.g. boundary:postal_code ...'''
date = "2015-09-24T16:34:00Z"
lastmod = "2015-09-25T12:54:00Z"
weight = 45567
keywords = [ "nominatim" ]
aliases = [ "/questions/45567" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to configure Nominatim?](/questions/45567/how-to-configure-nominatim)

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
<span id="post-45567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45567-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I would like to limit the list of OSM tags my Nominatim server makes use of. I found:</p>
<ul>
<li>The file <a href="https://github.com/twain47/Nominatim/blob/80df4d3b560f5b1fd550dcf8cdc09a992b69fee0/settings/phrase_settings.php">phrase_settings.php</a> with a blacklist and a whitelist but the default values don't look as if they would be valid.</li>
<li>The file <a href="https://github.com/twain47/Nominatim/blob/80df4d3b560f5b1fd550dcf8cdc09a992b69fee0/settings/partitionedtags.def">partitionedtags.def</a> but it seems to be incomplete. E.g. boundary:postal_code is not in there but AFAIK Nominatim uses it.</li>
</ul>
<p>I couldn't find any documentation. Anyone knows?</p>
<p>Best, Helge</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Sep '15, 16:34</strong></p>
<img src="https://secure.gravatar.com/avatar/71f1bd892495ccdeace17971dc5e6404?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Helge%20Fahrnberger&#39;s gravatar image" />
<p><span>Helge Fahrnb...</span><br />
<span class="score" title="111 reputation points">111</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Helge Fahrnberger has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-45567" class="comments-container">
&#10;</div>
<div id="comment-tools-45567" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45567-form-container" class="comment-form-container">
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

<span id="45577"></span>

<div id="answer-container-45577" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45577-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-45577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no simple configuration file for the tag selection. Tag processing is (still) hard-coded, so you have to hack a bit of code to achieve what you want.</p>
<p>The main tag filtering and categorizing happens in <code>osm2pgsql/output-gazetteer.cpp</code>. In particular, you should have a look at the function <code>place_tag_processor::process_tags()</code>. This function is called for each OSM object and goes through its list of tags. You can simply comment out all the tags you are not interested in.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '15, 20:52</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-45577" class="comments-container">
<span id="45593"></span>
<div id="comment-45593" class="comment">
<div id="post-45593-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's great, thank you! So the two settings files are to be ignored, right?</p>
</div>
<div id="comment-45593-info" class="comment-info">
<span class="comment-age">(25 Sep '15, 11:07)</span> <span class="comment-user userinfo">Helge Fahrnb...</span>
</div>
</div>
<span id="45599"></span>
<div id="comment-45599" class="comment">
<div id="post-45599-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes, the files can be ignored. phrase_settings.php is used only when importing special phrases from the Wiki and partitionedtags.def isn't used at all anymore.</p>
</div>
<div id="comment-45599-info" class="comment-info">
<span class="comment-age">(25 Sep '15, 12:54)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-45577" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45577-form-container" class="comment-form-container">
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

