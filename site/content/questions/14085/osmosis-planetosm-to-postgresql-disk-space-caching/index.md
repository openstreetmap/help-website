+++
type = "question"
title = "Osmosis Planet.osm to PostgreSQL disk space / caching"
description = '''Hey guys, I&#x27;m trying to dump a recent planet.osm file to a local PostgreSQL database on OS X.  I&#x27;m running a 120 GB SSD for my system drive, and a 500GB 7200RPM external drive for the database connected via Firewire 800. When I run osmosis with a simple read-xml, write-pgsql command I notice my syst...'''
date = "2012-07-08T21:59:00Z"
lastmod = "2012-07-10T22:36:00Z"
weight = 14085
keywords = [ "planet", "disk", "drive", "osmosis", "space" ]
aliases = [ "/questions/14085" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis Planet.osm to PostgreSQL disk space / caching](/questions/14085/osmosis-planetosm-to-postgresql-disk-space-caching)

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
<span id="post-14085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14085-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey guys, I'm trying to dump a recent planet.osm file to a local PostgreSQL database on OS X.</p>
<p>I'm running a 120 GB SSD for my system drive, and a 500GB 7200RPM external drive for the database connected via Firewire 800.</p>
<p>When I run osmosis with a simple read-xml, write-pgsql command I notice my system drive (the SSD) in activity manager fills up while my database (on the 500GB external drive) isn't being populated at all, or used at all.</p>
<p>It's on this step: <code>Processing input data, building geometries and creating database load files.</code></p>
<p>Obviously the SSD isn't large enough to handle whatever operations are being cached / created. So my question is, what is osmosis creating in the background and is there a way to force it to utilize the other volume instead of the system default?</p>
<p>After some testing, I believe that Osmosis is utilizing the temp folder on OS X, which is why I am seeing drive usage on my system drive/my SSD.</p>
<p>I am unsure if I can relocated the temp folder or if Java / Osmosis can told made to use another directory.</p>
<p>THANKS! -Cody</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-disk" rel="tag" title="see questions tagged &#39;disk&#39;">disk</span> <span class="post-tag tag-link-drive" rel="tag" title="see questions tagged &#39;drive&#39;">drive</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-space" rel="tag" title="see questions tagged &#39;space&#39;">space</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jul '12, 21:59</strong></p>
<img src="https://secure.gravatar.com/avatar/aa9f28cc449a272dbd654e8edf660877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Smartkid&#39;s gravatar image" />
<p><span>Smartkid</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Smartkid has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jul '12, 23:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-14085" class="comments-container">
&#10;</div>
<div id="comment-tools-14085" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14085-form-container" class="comment-form-container">
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

<span id="14090"></span>

<div id="answer-container-14090" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14090-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-14090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can set a different temporary directory with the command</p>
<pre><code>export JAVACMD_OPTIONS=&quot;-Djava.io.tmpdir=/dir/to/osm/tmp&quot;</code></pre>
<p>Also read the information about the <code>nodeLocationStorage</code> parameter on the <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.41#--write-pgsql_.28--wp.29">Osmosis wiki page</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '12, 23:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-14090" class="comments-container">
<span id="14155"></span>
<div id="comment-14155" class="comment">
<div id="post-14155-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks so much, this worked like a charm.</p>
<p>For those who are following, running the JAVACMD_OPTIONS line above will move the location on disk that Java uses as a temporary directory.</p>
<p>In my case, the default was OS X's temp dir which is automatically emptied on system restart. When I moved Java's tmp dir, an artifact was that Java's temp files are no longer automatically removed on system restart. You can simply delete the content of the folder you choose and/or reset the Java tmp dir afterwards.</p>
<p>Anyway, thanks Frederik! -Cody</p>
</div>
<div id="comment-14155-info" class="comment-info">
<span class="comment-age">(10 Jul '12, 22:36)</span> <span class="comment-user userinfo">Smartkid</span>
</div>
</div>
</div>
<div id="comment-tools-14090" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14090-form-container" class="comment-form-container">
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

