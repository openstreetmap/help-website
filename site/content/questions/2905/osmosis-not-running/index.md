+++
type = "question"
title = "Osmosis not running"
description = '''I am on a VPS running Debian 4 on Dreamhost, and am having problems running an extract on planet-latest.osm.bz2 bzcat planet-latest.osm.bz2 | osmosis&#92;  -read-xml enableDateParsing=no file=/dev/stdin&#92;  --bounding-box top=50.2866 left=-123.1448 bottom=49.8866 right=-122.7448--write-xml file=-&#92;  | bzip...'''
date = "2011-02-10T19:41:00Z"
lastmod = "2011-03-04T06:16:00Z"
weight = 2905
keywords = [ "planet", "extract", "java", "osmosis" ]
aliases = [ "/questions/2905" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis not running](/questions/2905/osmosis-not-running)

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
<span id="post-2905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2905-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am on a VPS running Debian 4 on Dreamhost, and am having problems running an extract on planet-latest.osm.bz2</p>
<pre><code>bzcat planet-latest.osm.bz2 | osmosis\
 -read-xml enableDateParsing=no file=/dev/stdin\
 --bounding-box top=50.2866 left=-123.1448 bottom=49.8866 right=-122.7448--write-xml file=-\
 | bzip2 &gt; extracted.osm.bz2</code></pre>
<p>Yields</p>
<pre><code>Exception in thread &quot;main&quot; java.lang.NoClassDefFoundError: org/codehaus/classworlds/Launcher
Caused by: java.lang.ClassNotFoundException: org.codehaus.classworlds.Launcher
        at java.net.URLClassLoader$1.run(URLClassLoader.java:200)
        at java.security.AccessController.doPrivileged(Native Method)
        at java.net.URLClassLoader.findClass(URLClassLoader.java:188)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:306)
        at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:276)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:251)
        at java.lang.ClassLoader.loadClassInternal(ClassLoader.java:319)</code></pre>
<p>How do I fix this? Also does anyone now how long an extract like this would take? I only have 300mb of dedicated RAM but more available for short periods of time.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '11, 19:41</strong></p>
<img src="https://secure.gravatar.com/avatar/3a5c89275037ff2627640835b33e9483?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbski&#39;s gravatar image" />
<p><span>wbski</span><br />
<span class="score" title="146 reputation points">146</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbski has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-2905" class="comments-container">
&#10;</div>
<div id="comment-tools-2905" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2905-form-container" class="comment-form-container">
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

<span id="3510"></span>

<div id="answer-container-3510" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3510-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3510-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-3510-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Found the problem. Have to execute Osmosis from the directory above the bin directory</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '11, 06:16</strong></p>
<img src="https://secure.gravatar.com/avatar/3a5c89275037ff2627640835b33e9483?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbski&#39;s gravatar image" />
<p><span>wbski</span><br />
<span class="score" title="146 reputation points">146</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbski has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-3510" class="comments-container">
&#10;</div>
<div id="comment-tools-3510" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3510-form-container" class="comment-form-container">
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

