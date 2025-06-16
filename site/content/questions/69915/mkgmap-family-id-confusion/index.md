+++
type = "question"
title = "mkgmap family-id confusion"
description = '''Hi I&#x27;m failing to understand how family-id works. I&#x27;m using the latest mkgmap to compile a custom map: java -Xms1024m -Xmx1024m -jar &quot;mkgmap.jar&quot; --gmapsupp --tdbfile --family-id=42 --style-file=&quot;generic new&quot; &quot;2000.typ&quot; &quot;Shepton.gz&quot;  This produces a map that&#x27;s viewable in Garmin Basecamp, but doesn&#x27;...'''
date = "2019-07-07T13:49:00Z"
lastmod = "2019-07-09T18:45:00Z"
weight = 69915
keywords = [ "mkgmap", "garmin", "family-id" ]
aliases = [ "/questions/69915" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [mkgmap family-id confusion](/questions/69915/mkgmap-family-id-confusion)

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
<span id="post-69915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69915-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I'm failing to understand how family-id works. I'm using the latest mkgmap to compile a custom map:</p>
<pre><code>java -Xms1024m -Xmx1024m -jar &quot;mkgmap.jar&quot; --gmapsupp --tdbfile --family-id=42 --style-file=&quot;generic new&quot; &quot;2000.typ&quot; &quot;Shepton.gz&quot;</code></pre>
<p>This produces a map that's viewable in Garmin Basecamp, but doesn't look as expected</p>
<p>I'm using <a href="https://sites.google.com/site/openfietsmap/procedure">OpenFietsMap's</a> style &amp; typ files from: <a href="https://github.com/ligfietser/mkgmap-style-sheets">https://github.com/ligfietser/mkgmap-style-sheets</a></p>
<p><a href="https://wiki.openstreetmap.org/wiki/Mkgmap/help/options#Product_description_options">https://wiki.openstreetmap.org/wiki/Mkgmap/help/options#Product_description_options</a></p>
<p>This section of the wiki says: "If you want to compile a map with a TYP file, you will need to ensure that the family-id of the map matches that of the TYP file"</p>
<p>If you view 2000.txt from the github you'll see the FID is set to 2000 <a href="https://github.com/ligfietser/mkgmap-style-sheets/tree/master/typ/osm%20generic%20new">https://github.com/ligfietser/mkgmap-style-sheets/tree/master/typ/osm%20generic%20new</a></p>
<p>However if I change --family-id=42 in the command line to 2000 Basecamp issues this error message &amp; won't open:</p>
<p><img src="/upfiles/Capture_vzQSXou.JPG" alt="alt text" /></p>
<p>What is the solution?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mkgmap" rel="tag" title="see questions tagged &#39;mkgmap&#39;">mkgmap</span> <span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span> <span class="post-tag tag-link-family-id" rel="tag" title="see questions tagged &#39;family-id&#39;">family-id</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '19, 13:49</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jul '19, 16:54</strong> </span></p>
</div>
</div>
<div id="comments-container-69915" class="comments-container">
<span id="69919"></span>
<div id="comment-69919" class="comment">
<div id="post-69919-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would use MapSetToolkit to manipulate this type of thing: which are Windows Registry entries IIRC. I'm not sure where you'd find it now, but I still find it useful.</p>
</div>
<div id="comment-69919-info" class="comment-info">
<span class="comment-age">(07 Jul '19, 20:44)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="69948"></span>
<div id="comment-69948" class="comment">
<div id="post-69948-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've been using MapSetToolkit occasionally for a few years, but I want to use mkgmap command line options within script to semi automate the process. MapSetToolkit's GUI means filling in the options <em>every</em> time. A real pain if your experimenting while learning to use it.</p>
<p>Also, unless I'm mistaken, it doesn't create a gmapsupp.img required for a Garmin GPSr</p>
</div>
<div id="comment-69948-info" class="comment-info">
<span class="comment-age">(09 Jul '19, 17:24)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="69951"></span>
<div id="comment-69951" class="comment">
<div id="post-69951-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you're changing the family ID in the files but not updating the respective registry values with MapSetToolkit, then BaseCamp isn't able to find what it's expecting. When the family ID changes, the filenames of the TDB and IMG files change too, so these all need to be updated in the registry.</p>
</div>
<div id="comment-69951-info" class="comment-info">
<span class="comment-age">(09 Jul '19, 18:45)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-69915" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69915-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

