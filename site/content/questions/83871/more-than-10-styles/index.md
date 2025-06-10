+++
type = "question"
title = "more than 10 styles"
description = '''Hi there, i have my own osm tile server. Everything works so far but i have one problem. I have more than 10 styles to pre render and offer to customers. But when i add more than 10 styles to renderd.conf i get the error &quot;More than 10 styles...&quot; where can i set up this. Please help Thank you'''
date = "2022-03-15T21:11:00Z"
lastmod = "2022-03-15T22:15:00Z"
weight = 83871
keywords = [ "limitations", "style" ]
aliases = [ "/questions/83871" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [more than 10 styles](/questions/83871/more-than-10-styles)

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
<span id="post-83871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83871-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there, i have my own osm tile server. Everything works so far but i have one problem. I have more than 10 styles to pre render and offer to customers. But when i add more than 10 styles to renderd.conf i get the error "More than 10 styles..." where can i set up this.</p>
<p>Please help</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-limitations" rel="tag" title="see questions tagged &#39;limitations&#39;">limitations</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Mar '22, 21:11</strong></p>
<img src="https://secure.gravatar.com/avatar/bcd5d57b0a8dbe3e71efb99db0935b14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zuane&#39;s gravatar image" />
<p><span>Zuane</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zuane has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Mar '22, 21:11</strong> </span></p>
</div>
</div>
<div id="comments-container-83871" class="comments-container">
&#10;</div>
<div id="comment-tools-83871" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83871-form-container" class="comment-form-container">
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

<span id="83872"></span>

<div id="answer-container-83872" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83872-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a compile-time setting in renderd, see <a href="https://github.com/openstreetmap/mod_tile/blob/acb11808d62a81b2d2c357425ea0917bc55631a3/includes/render_config.h#L52">https://github.com/openstreetmap/mod_tile/blob/acb11808d62a81b2d2c357425ea0917bc55631a3/includes/render_config.h#L52</a> - you need to re-compile renderd to change this.</p>
<p>Alternatively, swap out renderd with tirex <a href="https://github.com/openstreetmap/tirex">(https://github.com/openstreetmap/tirex)</a> which has no such limitation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Mar '22, 21:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Mar '22, 22:00</strong> </span></p>
</div>
</div>
<div id="comments-container-83872" class="comments-container">
<span id="83873"></span>
<div id="comment-83873" class="comment">
<div id="post-83873-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wow Frederik, this was fast. But sorry, i dont know where to find the file in wich i have to change this line. Can you please point me there.</p>
</div>
<div id="comment-83873-info" class="comment-info">
<span class="comment-age">(15 Mar '22, 21:42)</span> <span class="comment-user userinfo">Zuane</span>
</div>
</div>
<span id="83876"></span>
<div id="comment-83876" class="comment">
<div id="post-83876-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The following general information holds true for almost all Linux distributions: If you are told that you need to "compile" a piece of software that means that you will have to leave your usual "use package manager to install software" workflow. You will instead have to (1) download the source code, (2) install a software building environment, (3) compile the source code and possibly build a new package to install.</p>
<p>On a Debian or Ubuntu system, you can usually do <code>apt source renderd</code> which will download the source code for you, then you can make the modification you want. You might need to <code>apt install build-essential</code> or something to get the software build system installed. After than you will likely be able to run <code>debuild</code> to build a modified package (it might tell you to install additionall development packages first) that you can then install with <code>dpkg -i</code>.</p>
<p>If at all possible, ignore any instructions that tell you to "make install" or something like that, because these will install the software on your system bypassing the package manager and there will be no end of confusion especially if you are not an experienced sysadmin.</p>
</div>
<div id="comment-83876-info" class="comment-info">
<span class="comment-age">(15 Mar '22, 22:15)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-83872" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83872-form-container" class="comment-form-container">
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

