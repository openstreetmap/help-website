+++
type = "question"
title = "White screen on Arch startup"
description = '''I&#x27;m trying to run JOSM on arch linux. I tried both the josm(-svn) from the AUR, the jnlp and the jar version from https://josm.openstreetmap.de/. If I run the program, the loading screen works:  Unfortunately, after that one is finished, I receive an empty (white) screen:  If I enable debug logs (ja...'''
date = "2022-09-13T07:50:00Z"
lastmod = "2022-09-14T12:59:00Z"
weight = 85611
keywords = [ "help" ]
aliases = [ "/questions/85611" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [White screen on Arch startup](/questions/85611/white-screen-on-arch-startup)

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
<span id="post-85611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85611-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to run JOSM on arch linux. I tried both the josm(-svn) from the AUR, the jnlp and the jar version from <a href="https://josm.openstreetmap.de/.">https://josm.openstreetmap.de/.</a></p>
<p>If I run the program, the loading screen works: <img src="https://i.ibb.co/ZdVVGDF/tmp.png" alt="alt text" /></p>
<p>Unfortunately, after that one is finished, I receive an empty (white) screen:</p>
<p><img src="https://i.ibb.co/w0HGSf4/tmp.png" alt="alt text" /></p>
<p>If I enable debug logs (<code>java -jar josm-tested.jar --debug</code>), I don't see any errors, here's the log: <a href="https://textbin.net/raw/qcklqkrlkm">https://textbin.net/raw/qcklqkrlkm</a></p>
<p>Does anyone have an idea how to get JOSM to run?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '22, 07:50</strong></p>
<img src="https://secure.gravatar.com/avatar/d803f4390e9df4f92a98331b5e04648c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_Philipp&#39;s gravatar image" />
<p><span>H_Philipp</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_Philipp has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Sep '22, 07:53</strong> </span></p>
</div>
</div>
<div id="comments-container-85611" class="comments-container">
<span id="85612"></span>
<div id="comment-85612" class="comment">
<div id="post-85612-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which Java/JRE version are you using?</p>
</div>
<div id="comment-85612-info" class="comment-info">
<span class="comment-age">(13 Sep '22, 08:08)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="85613"></span>
<div id="comment-85613" class="comment">
<div id="post-85613-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm on 'openjdk 17.0.4.1 2022-08-12'</p>
</div>
<div id="comment-85613-info" class="comment-info">
<span class="comment-age">(13 Sep '22, 08:10)</span> <span class="comment-user userinfo">H_Philipp</span>
</div>
</div>
<span id="85619"></span>
<div id="comment-85619" class="comment">
<div id="post-85619-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Strange. I'm using openjdk 17.0.4 on Debian without such problems.</p>
</div>
<div id="comment-85619-info" class="comment-info">
<span class="comment-age">(14 Sep '22, 07:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="85621"></span>
<div id="comment-85621" class="comment">
<div id="post-85621-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could it be that you are using Wayland? As far as I know some people have problems running JOSM with Wayland, others don't. I don't know any details since I haven't switched to Wayland yet.</p>
</div>
<div id="comment-85621-info" class="comment-info">
<span class="comment-age">(14 Sep '22, 11:11)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="85622"></span>
<div id="comment-85622" class="comment">
<div id="post-85622-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you are using Wayland then try to set <code>_JAVA_AWT_WM_NONREPARENTING=1</code> before running JOSM. See <a href="https://discourse.ubuntu.com/t/environment-variables-for-wayland-hackers/12750.">https://discourse.ubuntu.com/t/environment-variables-for-wayland-hackers/12750.</a></p>
</div>
<div id="comment-85622-info" class="comment-info">
<span class="comment-age">(14 Sep '22, 12:08)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-85611" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85611-form-container" class="comment-form-container">
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

<span id="85623"></span>

<div id="answer-container-85623" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85623-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="H_Philipp has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try setting <code>sun.java2d.opengl=False</code> in your java configuration. If you're using an nVidia GPU, this is almost certainly the fix.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Sep '22, 12:59</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</img>
</div>
</div>
<div id="comments-container-85623" class="comments-container">
&#10;</div>
<div id="comment-tools-85623" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85623-form-container" class="comment-form-container">
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

