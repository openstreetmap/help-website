+++
type = "question"
title = "System configuration for optimal nominatim install"
description = '''Hi guys I promise this is the last question I ask of nominatim!! I have a new machine with 500 gb HD and 16 gb RAM. I will install centOS 6.6 on this and I would like to know how to partition the drive. Because if I do the normal configuration as follow: 50 gb root &#x27;a little&#x27; for boot 32 gb swap &#x27;re...'''
date = "2015-10-28T11:33:00Z"
lastmod = "2015-10-29T14:33:00Z"
weight = 46169
keywords = [ "nominatim" ]
aliases = [ "/questions/46169" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [System configuration for optimal nominatim install](/questions/46169/system-configuration-for-optimal-nominatim-install)

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
<span id="post-46169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46169-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys I promise this is the last question I ask of nominatim!!</p>
<p>I have a new machine with 500 gb HD and 16 gb RAM. I will install centOS 6.6 on this and I would like to know how to partition the drive.</p>
<p>Because if I do the normal configuration as follow:</p>
<pre><code>50 gb root
&#39;a little&#39; for boot
32 gb swap
&#39;rest&#39; for /usr or /home</code></pre>
<p>And I will install postgresql by yum, I will need to create a cluster for postgres because, with yum, the data folder will be placed under <code>/var/lib/pgsql/9.4/data</code> and I think this is under <code>/root</code></p>
<p>Than is madness to create a system as follows:</p>
<pre><code>&#39;a little&#39; for boot
32 gb swap
rest for /root</code></pre>
<p>?? What would be the optimum configuration knowing that I have to install postgres with yum??</p>
<p>Thanks a lot</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '15, 11:33</strong></p>
<img src="https://secure.gravatar.com/avatar/e6e1580c3bf447dab7c4a377186b60dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="giacomo-keybiz&#39;s gravatar image" />
<p><span>giacomo-keybiz</span><br />
<span class="score" title="33 reputation points">33</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="giacomo-keybiz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Oct '15, 14:05</strong> </span></p>
</div>
</div>
<div id="comments-container-46169" class="comments-container">
<span id="46170"></span>
<div id="comment-46170" class="comment">
<div id="post-46170-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How can <code>/var/lib/pgsql/9.4/data</code> be located under <code>/root</code>? These are completely different paths. Usually <code>/root</code> will never ever contain any large data, just a few tiny config files. I think misread <em>root</em> to be <code>/root</code> although it was meant to refer to '<code>/</code>' which is also called the <em>root</em> directory.</p>
</div>
<div id="comment-46170-info" class="comment-info">
<span class="comment-age">(28 Oct '15, 11:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="46218"></span>
<div id="comment-46218" class="comment">
<div id="post-46218-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes Scai you're right. I mean "/" partition. The problem is that if I create a default centOS machine the system will configurate as follow (for example on a 500gb disk):</p>
<pre><code>50 gb for / or /root
500 mb for /boot
4 gb for /swap
rest for /home</code></pre>
<p>Then when I go to install postgresql by yum, it put the <code>data</code> folder under <code>/var/lib/pgsql/9.4/</code> and it is surely under "/" because it has 50gb free space.</p>
<p>Now I can't install postgresql manually and I need more space for the data folder, then I create a postgres cluster but I prefer don't do it again...</p>
<p>For these reasons I asked if there is an optimal configuration for this job (nominatim). The machine is been created just for this. Is a server in wich I will install just nominatim and graphhopper.. stop.</p>
<p>Thanks.</p>
</div>
<div id="comment-46218-info" class="comment-info">
<span class="comment-age">(29 Oct '15, 14:06)</span> <span class="comment-user userinfo">giacomo-keybiz</span>
</div>
</div>
<span id="46220"></span>
<div id="comment-46220" class="comment">
<div id="post-46220-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Then assign more space for "/" during installation and less to /home which you won't really need. There is no "optimal" configuration, just make sure you have enough disk space for your database. It won't run faster or slower if you assign more or less space to /boot or /swap.</p>
</div>
<div id="comment-46220-info" class="comment-info">
<span class="comment-age">(29 Oct '15, 14:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46169" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46169-form-container" class="comment-form-container">
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

<span id="46219"></span>

<div id="answer-container-46219" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46219-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46219-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46219-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From memory Redhat and derivatives have always had that "odd" approach to partitioning. Given that you won't have huge /home directories, I'd explicity remove those and allocate "the rest of the disk" to /, since you don't want to create an artifical point of failure where a partition is full. How hard the installation process will make this task for you I don't know, because I haven't installed a vanilla Redhat system for a while.</p>
<p>One other thing to watch for - check the version of any frequently-updated package (such as Postgres) that yum offers against the latest source version to make sure you aren't installing a very out-of-date version. I don't know that it'll be a problem, but it's something to check.</p>
<p>You've probably already seen the page in the wiki; if not:</p>
<p><a href="http://wiki.openstreetmap.org/w/index.php?title=Nominatim/Installation_on_CentOS&amp;oldid=1180464">http://wiki.openstreetmap.org/w/index.php?title=Nominatim/Installation_on_CentOS&amp;oldid=1180464</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Oct '15, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-46219" class="comments-container">
&#10;</div>
<div id="comment-tools-46219" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46219-form-container" class="comment-form-container">
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

