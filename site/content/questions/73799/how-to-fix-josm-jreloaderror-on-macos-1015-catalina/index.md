+++
type = "question"
title = "How to fix JOSM JRELoadError on macOS 10.15 Catalina?"
description = '''When I run brew cask install josm or download the latest JOSM ZIP, I get JRELoadError. Homebrew suggests installing OpenJDK with brew cask install adoptopenjdk but it does not fix anything. Can Homebrew properly install JOSM and Java? openjdk version &quot;14&quot; 2020-03-17  OpenJDK Runtime Environment (bui...'''
date = "2020-03-27T18:47:00Z"
lastmod = "2020-10-11T19:09:00Z"
weight = 73799
keywords = [ "josm", "macosx", "java", "installation", "homebrew" ]
aliases = [ "/questions/73799" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to fix JOSM JRELoadError on macOS 10.15 Catalina?](/questions/73799/how-to-fix-josm-jreloaderror-on-macos-1015-catalina)

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
<span id="post-73799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73799-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I run <code>brew cask install josm</code> or download the latest JOSM ZIP, I get <strong>JRELoadError</strong>.</p>
<p>Homebrew suggests installing OpenJDK with <code>brew cask install adoptopenjdk</code> but it does not fix anything.</p>
<p>Can Homebrew properly install JOSM and Java?</p>
<p>openjdk version "14" 2020-03-17 OpenJDK Runtime Environment (build 14+36-1461) OpenJDK 64-Bit Server VM (build 14+36-1461, mixed mode, sharing)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-macosx" rel="tag" title="see questions tagged &#39;macosx&#39;">macosx</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-homebrew" rel="tag" title="see questions tagged &#39;homebrew&#39;">homebrew</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Mar '20, 18:47</strong></p>
<img src="https://secure.gravatar.com/avatar/103cc0cc7cf17e85b013c858d83bd93c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="homocomputeris&#39;s gravatar image" />
<p><span>homocomputeris</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="homocomputeris has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Mar '20, 11:42</strong> </span></p>
</div>
</div>
<div id="comments-container-73799" class="comments-container">
&#10;</div>
<div id="comment-tools-73799" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73799-form-container" class="comment-form-container">
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

<span id="73809"></span>

<div id="answer-container-73809" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73809-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Solved by installing Java 8u241 from java.com instead of Homebrew.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '20, 12:55</strong></p>
<img src="https://secure.gravatar.com/avatar/103cc0cc7cf17e85b013c858d83bd93c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="homocomputeris&#39;s gravatar image" />
<p><span>homocomputeris</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="homocomputeris has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73809" class="comments-container">
<span id="77044"></span>
<div id="comment-77044" class="comment">
<div id="post-77044-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I installed JOSM with <code>brew</code>, nonetheless the same error was only fixed by installing Java from java.com</p>
</div>
<div id="comment-77044-info" class="comment-info">
<span class="comment-age">(11 Oct '20, 19:09)</span> <span class="comment-user userinfo">habi</span>
</div>
</div>
</div>
<div id="comment-tools-73809" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73809-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73803"></span>

<div id="answer-container-73803" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73803-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73803-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73803-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Wow! I hadn't thought about trying to install JOSM via brew.</p>
<p>Seems unlikely to me that the Homebrew maintainers would be on as active and frequent update cycle as getting the jar from the people maintaining JOSM so you'd likely always be running an older version.</p>
<p>I just have a Java VM environment and download the latest josm-tested.jar file from <a href="https://josm.openstreetmap.de">https://josm.openstreetmap.de</a> every time JOSM nags me that is it old (about once a month). Only issue is that each time I download a new version I have to tell the MacOS that it is safe to run it. I am still on Mohave as there are some programs I have that won't run on newer MacOS versions so I am not sure if what I am doing will work for you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '20, 01:17</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-73803" class="comments-container">
<span id="73805"></span>
<div id="comment-73805" class="comment">
<div id="post-73805-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I always download the jar file and run it from the terminal window. I do get asked to keep the file before download, but I do not get additional questions when I run the program.</p>
</div>
<div id="comment-73805-info" class="comment-info">
<span class="comment-age">(28 Mar '20, 06:37)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="73807"></span>
<div id="comment-73807" class="comment">
<div id="post-73807-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It turns out that it's not a Homebrew issue.</p>
</div>
<div id="comment-73807-info" class="comment-info">
<span class="comment-age">(28 Mar '20, 11:31)</span> <span class="comment-user userinfo">homocomputeris</span>
</div>
</div>
</div>
<div id="comment-tools-73803" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73803-form-container" class="comment-form-container">
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

