+++
type = "question"
title = "How can I get osmosis to use more than two CPUs/cores?"
description = '''The simplest version of the command I&#x27;m using is (pretty formatting for easier reading - it&#x27;s usually one line): osmosis --read-pbf-fast file=&quot;north-america-latest.osm.pbf&quot;   --bounding-polygon file=&quot;holyoke_ma.poly&quot; --write-xml file=&quot;holyoke_ma.osm&quot;  I get more complex by adding --tee ## with ## be...'''
date = "2014-01-16T19:12:00Z"
lastmod = "2014-01-16T19:37:00Z"
weight = 29892
keywords = [ "pbf", "polygon", "osmosis" ]
aliases = [ "/questions/29892" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I get osmosis to use more than two CPUs/cores?](/questions/29892/how-can-i-get-osmosis-to-use-more-than-two-cpuscores)

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
<span id="post-29892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29892-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The simplest version of the command I'm using is (pretty formatting for easier reading - it's usually one line):</p>
<pre><code>osmosis --read-pbf-fast file=&quot;north-america-latest.osm.pbf&quot; 
        --bounding-polygon file=&quot;holyoke_ma.poly&quot; --write-xml file=&quot;holyoke_ma.osm&quot;</code></pre>
<p>I get more complex by adding <code>--tee ##</code> with <code>##</code> being the number of files being read/written. So that's something like (pretty formatting for easier reading - it's usually one line):</p>
<pre><code>osmosis --read-pbf-fast file=&quot;north-america-latest.osm.pbf&quot; --tee 4 
        --bounding-polygon file=&quot;city1.poly&quot; --write-xml file=&quot;city1.osm&quot;
        --bounding-polygon file=&quot;city2.poly&quot; --write-xml file=&quot;city2.osm&quot;
        --bounding-polygon file=&quot;city3.poly&quot; --write-xml file=&quot;city3.osm&quot;
        --bounding-polygon file=&quot;city4.poly&quot; --write-xml file=&quot;city4.osm&quot;</code></pre>
<p>I've tried adding <code>workers=##</code> to the mix, with <code>##</code> being the number of cores on the server. That results in something like (pretty formatting for easier reading - it's usually one line):</p>
<pre><code>osmosis --read-pbf-fast workers=4 file=&quot;north-america-latest.osm.pbf&quot; --tee 4 
        --bounding-polygon file=&quot;city1.poly&quot; --write-xml file=&quot;city1.osm&quot;
        --bounding-polygon file=&quot;city2.poly&quot; --write-xml file=&quot;city2.osm&quot;
        --bounding-polygon file=&quot;city3.poly&quot; --write-xml file=&quot;city3.osm&quot;
        --bounding-polygon file=&quot;city4.poly&quot; --write-xml file=&quot;city4.osm&quot;</code></pre>
<p>In any of my attempts, with 2 or more cores, the process tops out at nearly 200% CPU use (when viewed in <code>top</code>). When viewed in <code>mpstat -P ALL</code> (which you can get after running <code>apt-get install sysstat</code>), there's one CPU that usually sits at about 20-30%, and the others are mostly idle.</p>
<p>I verified that I can get a process to use all cores (4 in this case) by running <code>sysbench --test=cpu --cpu-max-prime=20000 --num-threads=4 run</code> (which you can get after running <code>apt-get install sysbench</code>) ... This would spike the process to 400% (when viewed in <code>top</code>).</p>
<ul>
<li>How do I get <code>osmosis</code> to use all of the available CPUs/cores?</li>
<li>Where (if anywhere) should <code>--buffer</code> entries be placed? Before the <code>--bounding-polygon</code> flag? Before the <code>--write-xml</code> flag?</li>
<li>Should I keep a limit to my <code>--tee</code> usage? Does that tie to the number of cores at all? Sometimes I have hundreds (up to a thousand or so) of <code>.poly</code> files to process - can I put them all into a single <code>osmosis</code> command with a very large <code>tee</code> value?</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jan '14, 19:12</strong></p>
<img src="https://secure.gravatar.com/avatar/0ada7b97d85873855231744286452af4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesChevalier&#39;s gravatar image" />
<p><span>JamesChevalier</span><br />
<span class="score" title="151 reputation points">151</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesChevalier has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-29892" class="comments-container">
&#10;</div>
<div id="comment-tools-29892" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29892-form-container" class="comment-form-container">
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

<span id="29893"></span>

<div id="answer-container-29893" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29893-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would suggest to place one "buffer" before and after each --bounding-polygon directive. I haven't tried more than about 50 "tee" threads but I guess more would still be possible - but keep in mind that the number of "point in polygon" checks that osmosis has to make is the size of your input file multiplied by the number of --bounding-polygon threads you're using - each object will be checked against all (thousands of) polygons. Therefore it is more efficient to first divide up your input file into a couple of smaller regions and extract your files from them.</p>
<p>Here's an <a href="http://blog.geofabrik.de/?p=75">older blog entry</a> that describes how we used to run the Geofabrik extracts. We nowadays use the <a href="https://github.com/MaZderMind/osm-history-splitter">history splitter</a> which offers better performance when doing a large number of polygon splits at once.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jan '14, 19:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-29893" class="comments-container">
<span id="29894"></span>
<div id="comment-29894" class="comment">
<div id="post-29894-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! (I actually came across your blog post the other day, and thought about contacting you directly). I've mostly used a country OSM file (like germany-latest.osm.pbf), but I did run some tests with a 'state' level file (like brandenburg-latest.osm.pbf). Those definitely finished quicker, but still didn't make full use of the CPU. I'll try again with your suggestion of <code>buffer</code> placement.</p>
</div>
<div id="comment-29894-info" class="comment-info">
<span class="comment-age">(16 Jan '14, 19:37)</span> <span class="comment-user userinfo">JamesChevalier</span>
</div>
</div>
</div>
<div id="comment-tools-29893" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29893-form-container" class="comment-form-container">
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

