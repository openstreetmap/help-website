+++
type = "question"
title = "[closed] How to install renderd as a service"
description = '''I have setup mod_tiles and the renderd binary that comes with it functions properly when run manually. I want to however make it run automatically when the server starts. I&#x27;m in linux. How can I do this? I am running Archlinux and it uses systemd to manage the startup services. Anyone has any knowle...'''
date = "2013-05-08T19:46:00Z"
lastmod = "2013-05-17T15:14:00Z"
weight = 22201
keywords = [ "setup", "renderd", "tileserver", "mod_tile" ]
aliases = [ "/questions/22201" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How to install renderd as a service](/questions/22201/how-to-install-renderd-as-a-service)

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
<span id="post-22201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22201-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have setup mod_tiles and the <strong>renderd</strong> binary that comes with it functions properly when run manually. I want to however make it run automatically when the server starts. I'm in linux. How can I do this?</p>
<p>I am running <strong>Archlinux</strong> and it uses systemd to manage the startup services. Anyone has any knowledge of this?</p>
<p>Even if someone has a knowledge in <strong>Debian</strong> or <strong>Ubuntu</strong>, I could try to convert it to Arch.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 May '13, 19:46</strong></p>
<img src="https://secure.gravatar.com/avatar/fce9c9c5dc42d98e71856d166e984e96?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bibstha&#39;s gravatar image" />
<p><span>bibstha</span><br />
<span class="score" title="76 reputation points">76</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bibstha has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>17 May '13, 15:14</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span></p>
</div>
</div>
<div id="comments-container-22201" class="comments-container">
<span id="22203"></span>
<div id="comment-22203" class="comment">
<div id="post-22203-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What distribution and version of Linux are you using? The way that you configure things to run in the background at system startup can vary somewhat.</p>
</div>
<div id="comment-22203-info" class="comment-info">
<span class="comment-age">(08 May '13, 21:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="22227"></span>
<div id="comment-22227" class="comment">
<div id="post-22227-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just updated the question.</p>
</div>
<div id="comment-22227-info" class="comment-info">
<span class="comment-age">(09 May '13, 16:03)</span> <span class="comment-user userinfo">bibstha</span>
</div>
</div>
<span id="22468"></span>
<div id="comment-22468" class="comment">
<div id="post-22468-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Installing renderd as a service on ArchLinux is just the same as <a href="http://blog.sdbarker.com/adding-custom-units-services-to-systemd-on-arch-linux/">creating a custom systemd service</a>.</p>
</div>
<div id="comment-22468-info" class="comment-info">
<span class="comment-age">(16 May '13, 09:39)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22201-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Pieren 17 May '13, 15:14

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22518"></span>

<div id="answer-container-22518" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22518-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-22518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use your prefered web search tool to find an how-to set-up a service at Archlinux boot. Your question is not related to OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '13, 15:14</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-22518" class="comments-container">
&#10;</div>
<div id="comment-tools-22518" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22518-form-container" class="comment-form-container">
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

