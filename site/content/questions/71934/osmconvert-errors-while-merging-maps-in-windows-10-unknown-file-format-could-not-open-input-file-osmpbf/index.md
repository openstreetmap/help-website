+++
type = "question"
title = "osmconvert - errors while merging maps in Windows 10 - unknown file format, could not open input file: .osm.pbf"
description = '''I&#x27;ve donwloaded the following maps: andorra-latest.osm.pbf https://download.geofabrik.de/europe/andorra-latest.osm.pbf azores-latest.osm.pbf https://download.geofabrik.de/europe/azores-latest.osm.pbf cyprus-latest.osm.pbf https://download.geofabrik.de/europe/cyprus-latest.osm.pbf  And I am using osm...'''
date = "2019-12-02T09:38:00Z"
lastmod = "2019-12-10T13:55:00Z"
weight = 71934
keywords = [ "openstreetmap", "merge", "osmconvert", "osm.pbf" ]
aliases = [ "/questions/71934" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [osmconvert - errors while merging maps in Windows 10 - unknown file format, could not open input file: .osm.pbf](/questions/71934/osmconvert-errors-while-merging-maps-in-windows-10-unknown-file-format-could-not-open-input-file-osmpbf)

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
<span id="post-71934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71934-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've donwloaded the following maps:</p>
<pre><code>andorra-latest.osm.pbf       https://download.geofabrik.de/europe/andorra-latest.osm.pbf
azores-latest.osm.pbf        https://download.geofabrik.de/europe/azores-latest.osm.pbf
cyprus-latest.osm.pbf        https://download.geofabrik.de/europe/cyprus-latest.osm.pbf</code></pre>
<p>And I am using <a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Windows">osmconvert</a> to merge maps. I read <a href="/questions/48843/merging-two-or-more-geographical-areas-to-import-two-or-more-osm-files-in-nominatim">this answer</a> to merge maps. So my command of merging the above maps looks like this:</p>
<pre><code>.\osmconvert andorra-latest.osm.pbf --out-o5m | .\osmconvert - azores-latest.osm.pbf | .\osmconvert - cyprus-latest.osm.pbf -o=all.osm.pbf</code></pre>
<p>However, the osmconvert shows the following errors after running the above command:</p>
<pre><code>osmconvert Error: unknown file format: standard input
osmconvert Error: could not open input file: .osm.pbf</code></pre>
<p>An image: <img src="/upfiles/osmoutput.png" alt="alt text" /></p>
<p>However, the merging perfectly works in Windows 7 and Windows Server 2016 Standard</p>
<p>Does anybody know how to solve this error?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-osm.pbf" rel="tag" title="see questions tagged &#39;osm.pbf&#39;">osm.pbf</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Dec '19, 09:38</strong></p>
<img src="https://secure.gravatar.com/avatar/cbd5c282ccb929604467e3b3f900b0d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CuriosityBeginner&#39;s gravatar image" />
<p><span>CuriosityBeg...</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CuriosityBeginner has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-71934" class="comments-container">
&#10;</div>
<div id="comment-tools-71934" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71934-form-container" class="comment-form-container">
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

<span id="71942"></span>

<div id="answer-container-71942" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71942-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="CuriosityBeginner has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to <a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Merging_two_or_more_Geographical_Areas">the documentation</a>, merging files can be done in one shot by listing all of the input files. In your case, the command would be simply:</p>
<pre><code>.\osmconvert andorra-latest.osm.pbf azores-latest.osm.pbf cyprus-latest.osm.pbf -o=all.osm.pbf</code></pre>
<p>EDIT: Apparently you can't merge like this with .osm.pbf files. You can with .o5m files.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '19, 18:19</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Dec '19, 17:15</strong> </span></p>
</div>
</div>
<div id="comments-container-71942" class="comments-container">
<span id="71950"></span>
<div id="comment-71950" class="comment">
<div id="post-71950-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks for your reply. However, it says <code>osmconvert Error: more than one.pbf input file is not allowed</code> Maybe you have other suggestions?</p>
</div>
<div id="comment-71950-info" class="comment-info">
<span class="comment-age">(02 Dec '19, 19:51)</span> <span class="comment-user userinfo">CuriosityBeg...</span>
</div>
</div>
<span id="71967"></span>
<div id="comment-71967" class="comment">
<div id="post-71967-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Looks like merging only works with format <code>o5m</code> and not with <code>pbf</code>. So you have to convert your files to <code>o5m</code> first: <code>osmconvert andorra-latest.osm.pbf -o=andorra-latest.osm.o5m</code>. Afterwards you can merge them. Not sure if the merge process is able to write them as pbf directly or if you need to write o5m again and convert it to pbf during an additional step.</p>
<p>Alternatively just use the more modern and faster <a href="http://osmcode.org/osmium-tool/">osmium-tool</a>: <code>osmium merge andorra-latest.osm.pbf azores-latest.osm.pbf cyprus-latest.osm.pbf -o all.osm.pbf</code>.</p>
</div>
<div id="comment-71967-info" class="comment-info">
<span class="comment-age">(03 Dec '19, 15:49)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="72058"></span>
<div id="comment-72058" class="comment">
<div id="post-72058-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a> how can I get exe of osmium-tool? Thanks in advance.</p>
</div>
<div id="comment-72058-info" class="comment-info">
<span class="comment-age">(10 Dec '19, 08:18)</span> <span class="comment-user userinfo">CuriosityBeg...</span>
</div>
</div>
<span id="72060"></span>
<div id="comment-72060" class="comment">
<div id="post-72060-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/17522/curiositybeginner">@CuriosityBeginner</a> As far as I know there are no official Windows builds available. Also see related discussions at <a href="https://github.com/osmcode/osmium-tool/issues/59">https://github.com/osmcode/osmium-tool/issues/59</a> and <a href="https://github.com/osmcode/osmium-tool/pull/105.">https://github.com/osmcode/osmium-tool/pull/105.</a> <a href="https://github.com/osmcode/osmium-tool#building">https://github.com/osmcode/osmium-tool#building</a> explains how to build it yourself using Visual Studio C++. On Linux, osmium-tool is available via the package manager on various distributions.</p>
</div>
<div id="comment-72060-info" class="comment-info">
<span class="comment-age">(10 Dec '19, 08:37)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="72063"></span>
<div id="comment-72063" class="comment">
<div id="post-72063-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a>: I would not recommend osmium tool for Windows users. Here the sensible approach is to convert each osm.pbf file into an o5m file (perhaps in a temporary working directory) &amp; then merge them as <a href="https://help.openstreetmap.org/users/8189/alester">@alester</a> says.</p>
</div>
<div id="comment-72063-info" class="comment-info">
<span class="comment-age">(10 Dec '19, 13:55)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71942" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71942-form-container" class="comment-form-container">
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

