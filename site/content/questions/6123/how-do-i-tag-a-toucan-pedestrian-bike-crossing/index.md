+++
type = "question"
title = "How do I tag a toucan (pedestrian + bike) crossing?"
description = '''A toucan crossing is a road crossing where pedestrians and bikes can cross together (typically used to cross a road between two segregated cycle paths). The OSM Wiki for &quot;crossing&quot; states that I can either use: highway=crossing crossing=traffic_signals bicycle=yes segregated=no crossing_ref=toucan  ...'''
date = "2011-07-01T09:19:00Z"
lastmod = "2011-07-05T15:01:00Z"
weight = 6123
keywords = [ "crossing", "tagging" ]
aliases = [ "/questions/6123" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I tag a toucan (pedestrian + bike) crossing?](/questions/6123/how-do-i-tag-a-toucan-pedestrian-bike-crossing)

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
<span id="post-6123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6123-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-6123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A <a href="http://en.wikipedia.org/wiki/Toucan_crossing">toucan crossing</a> is a road crossing where pedestrians and bikes can cross together (typically used to cross a road between two segregated cycle paths).</p>
<p>The <a href="http://wiki.openstreetmap.org/wiki/Key:crossing">OSM Wiki for "crossing"</a> states that I can either use:</p>
<pre><code>highway=crossing
crossing=traffic_signals
bicycle=yes
segregated=no
crossing_ref=toucan</code></pre>
<p>Or the "UK shortcut":</p>
<pre><code>crossing=toucan</code></pre>
<p>However the <code>crossing=toucan</code> version doesn't appear on the default Mapnik rendering on the OSM home page so I'm not sure how widely recognised it is (<a href="http://taginfo.openstreetmap.org/keys/?key=crossing#values">TagInfo suggests there are only around 1000 uses of <code>toucan</code></a>, compared to 64,000 of <code>traffic_signals</code>).</p>
<p>Despite this the <a href="http://www.gravitystorm.co.uk/shine/cycle-info/">"More Info" link from OpenCycleMap</a> suggests that it <em>only</em> recognises the <code>crossing=toucan</code> version and treats anything else as "Other Crossings". And the <a href="http://www.cyclestreets.net/journey/help/osmconversion/">OSM information on</a> <a href="http://CycleStreets.net">CycleStreets.net</a> suggests the same thing.</p>
<p>So which should I use? Is one method "better" than the other? Is there any reason that the Mapnik rendering can't recognise the UK shortcut or that OpenCycleMap can't recognise the long version?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-crossing" rel="tag" title="see questions tagged &#39;crossing&#39;">crossing</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jul '11, 09:19</strong></p>
<img src="https://secure.gravatar.com/avatar/f61876d1f1d2de794259119cdd596316?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GrahamS&#39;s gravatar image" />
<p><span>GrahamS</span><br />
<span class="score" title="3635 reputation points"><span>3.6k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="45 badges"><span class="silver">●</span><span class="badgecount">45</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GrahamS has 7 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jul '11, 09:31</strong> </span></p>
</div>
</div>
<div id="comments-container-6123" class="comments-container">
<span id="6135"></span>
<div id="comment-6135" class="comment">
<div id="post-6135-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>OpenCycleMap interprets three different ways of tagging toucan crossings - as well as the crossing=toucan method, it handles crossing_ref and also access-based crossing tagging. See <a href="https://gitorious.org/opencyclemap-tagtransform/opencyclemap-tagtransform/blobs/master/transform-crossings.xml">https://gitorious.org/opencyclemap-tagtransform/opencyclemap-tagtransform/blobs/master/transform-crossings.xml</a> for the gory details</p>
</div>
<div id="comment-6135-info" class="comment-info">
<span class="comment-age">(01 Jul '11, 15:08)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="6178"></span>
<div id="comment-6178" class="comment">
<div id="post-6178-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <span>@Andy</span> that's good to know. The OCM page I linked only mentions <code>crossing="toucan"</code> - perhaps it should be updated?</p>
</div>
<div id="comment-6178-info" class="comment-info">
<span class="comment-age">(05 Jul '11, 14:24)</span> <span class="comment-user userinfo">GrahamS</span>
</div>
</div>
<span id="6179"></span>
<div id="comment-6179" class="comment">
<div id="post-6179-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>what, to expose to normal people some of the worst of the OSM tagging nonsense? Explain that there's at least three different ways to tag one? I'm not going to inflict this on anyone :-)</p>
</div>
<div id="comment-6179-info" class="comment-info">
<span class="comment-age">(05 Jul '11, 15:01)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
</div>
<div id="comment-tools-6123" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6123-form-container" class="comment-form-container">
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

<span id="6143"></span>

<div id="answer-container-6143" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6143-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6143-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-6143-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GrahamS has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<h2 id="the-basics">The basics:</h2>
<p>As a minimum, use</p>
<pre><code>highway=crossing
crossing_ref=toucan</code></pre>
<p>Then it depends on whether you expect international application programmers to know what a "toucan crossing" is. If you don't want to rely on their knowledge of UK crossing terminology, you can add the additional tags that you quoted from the wiki.</p>
<h2 id="controversy-crossingtoucan-vs.-crossing_reftoucan">Controversy: crossing=toucan vs. crossing_ref=toucan:</h2>
<p>As you have noted, there is a popular alternative for crossing_ref=toucan, crossing=toucan. It's not obvious which you should choose, but I'll try to summarize the arguments again:</p>
<p>Pro crossing=toucan</p>
<ul>
<li>historically, crossing=toucan predates crossing_ref=toucan and even the international crossing tags</li>
<li>it is currently documented in the wiki (<a href="http://wiki.openstreetmap.org/w/index.php?title=Key%3Acrossing&amp;action=historysubmit&amp;diff=556201&amp;oldid=552677">attempts to change this have been reverted</a>)</li>
</ul>
<p>Pro crossing_ref=toucan</p>
<ul>
<li>it is used more frequently (<a href="http://taginfo.openstreetmap.org/tags/crossing_ref=toucan">1842</a> vs. <a href="http://taginfo.openstreetmap.org:8001/tags/crossing=toucan">1071</a>)</li>
<li>crossing=toucan conflicts with tags like crossing=traffic_signals (<a href="http://taginfo.openstreetmap.org/tags/crossing=traffic_signals#wiki">64,883 uses</a>), crossing_ref toucan can coexist</li>
<li>it is also documented on the wiki (but only as an add-on tag)</li>
<li>JOSM presets use this tag</li>
</ul>
<p>I would personally encourage the switch to crossing_ref, if for no other reason than allowing the supporters of "UK names" and "explicit subtagging" to peacefully coexist. Using crossing=toucan forces mappers into an avoidable conflict over the value for crossing tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jul '11, 20:04</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jul '11, 20:40</strong> </span></p>
</div>
</div>
<div id="comments-container-6143" class="comments-container">
&#10;</div>
<div id="comment-tools-6143" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6143-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6124"></span>

<div id="answer-container-6124" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6124-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-6124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The JOSM preset for Toucan crossing currently adds the tags</p>
<pre><code>highway=crossing
crossing_ref=toucan</code></pre>
<p>This seems to be a mistake, and as per the wiki and OCM recommendations I would suggest</p>
<pre><code>highway=crossing
crossing=toucan</code></pre>
<p>I wouldn't worry about what does or does not render on the Mapnik rendering too much, as there are too many things mapped for everything to show. If you are concerned though you could suggest an enhancement at <a href="http://trac.openstreetmap.org"></a><a href="http://trac.openstreetmap.org">trac.openstreetmap.org</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jul '11, 10:09</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-6124" class="comments-container">
<span id="6125"></span>
<div id="comment-6125" class="comment">
<div id="post-6125-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah I wouldn't normally worry too much about the Mapnik rendering - but <code>crossing=traffic_signals</code> does get rendered, so it's not like the general policy is to avoid rendering crossings for aesthetic reasons.</p>
</div>
<div id="comment-6125-info" class="comment-info">
<span class="comment-age">(01 Jul '11, 10:46)</span> <span class="comment-user userinfo">GrahamS</span>
</div>
</div>
<span id="6130"></span>
<div id="comment-6130" class="comment">
<div id="post-6130-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I've done a quick search and there is already <a href="http://trac.openstreetmap.org/ticket/3483">http://trac.openstreetmap.org/ticket/3483</a> suggesting highway=crossing be rendered.</p>
</div>
<div id="comment-6130-info" class="comment-info">
<span class="comment-age">(01 Jul '11, 11:46)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-6124" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6124-form-container" class="comment-form-container">
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

