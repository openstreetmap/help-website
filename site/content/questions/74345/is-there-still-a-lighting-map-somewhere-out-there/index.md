+++
type = "question"
title = "Is there still a lighting map somewhere out there?"
description = '''I only just now realized that ITO World have discontinued their map services last year. I had frequently used their &quot;Highway Lighting&quot; visualization of lit and unlit highways in the past. A similar service from University of Heidelberg has also not been maintained for a long time. Is there some map ...'''
date = "2020-04-23T10:43:00Z"
lastmod = "2020-11-04T11:04:00Z"
weight = 74345
keywords = [ "lit", "visualization", "lighting" ]
aliases = [ "/questions/74345" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there still a lighting map somewhere out there?](/questions/74345/is-there-still-a-lighting-map-somewhere-out-there)

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
<span id="post-74345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74345-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-74345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I only just now realized that ITO World have <a href="https://www.itoworld.com/ito-map-announcement/">discontinued their map services</a> last year. I had frequently used their "Highway Lighting" visualization of lit and unlit highways in the past. A similar service from <a href="https://www.geog.uni-heidelberg.de/gis/online.html">University of Heidelberg</a> has also not been maintained for a long time.</p>
<p>Is there some map out there that shows me which highways are tagged with a lit=yes, lit=no or no lit=* at all? Or how could I get Overpass Turbo to do that? I'm not really familiar with visualization options (different colors etc) there.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lit" rel="tag" title="see questions tagged &#39;lit&#39;">lit</span> <span class="post-tag tag-link-visualization" rel="tag" title="see questions tagged &#39;visualization&#39;">visualization</span> <span class="post-tag tag-link-lighting" rel="tag" title="see questions tagged &#39;lighting&#39;">lighting</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Apr '20, 10:43</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Apr '20, 20:52</strong> </span></p>
</div>
</div>
<div id="comments-container-74345" class="comments-container">
<span id="74347"></span>
<div id="comment-74347" class="comment">
<div id="post-74347-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I won't put this as an answer because I think you mean online slippy map specifically, but OsmAnd has the option to show lighting as an optional 'detail'. It places a yellow 'halo' on streets marked as lit, a orange ones around ones marked as unlit and leaves untagged streets halo free. The update frequency might be a little slow for your purposes (unless you have a live subscription).</p>
</div>
<div id="comment-74347-info" class="comment-info">
<span class="comment-age">(23 Apr '20, 20:39)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="74349"></span>
<div id="comment-74349" class="comment">
<div id="post-74349-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, you are right. I am looking for an online slippy map. But thanks anyway. I'll give it a shot if I don't find any better solution.</p>
</div>
<div id="comment-74349-info" class="comment-info">
<span class="comment-age">(23 Apr '20, 20:51)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="77201"></span>
<div id="comment-77201" class="comment">
<div id="post-77201-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Don’t know if you’ll see this, but I’ve been adding lighting simply as individual nodes (highway=streetlamp) for street lamps, so if you were to visualize a city with the suggestion given below, it wouldn’t work that well for some places. Just to keep in mind! :-)</p>
</div>
<div id="comment-77201-info" class="comment-info">
<span class="comment-age">(23 Oct '20, 14:03)</span> <span class="comment-user userinfo">IanVG</span>
</div>
</div>
<span id="77216"></span>
<div id="comment-77216" class="comment">
<div id="post-77216-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/18989/ianvg">@IanVG</a>: Yes, below code does not pick up street lamps on nodes but that could be easily added. For data consumers (e.g. calculate a route trying to only use lit streets) it's easier to evaluate the <code>lit=*</code> tag on the ways. Therefore I would always recommend tagging that as well when you tag individual street lamps.</p>
</div>
<div id="comment-77216-info" class="comment-info">
<span class="comment-age">(24 Oct '20, 17:51)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="77392"></span>
<div id="comment-77392" class="comment">
<div id="post-77392-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've updated the query to also look for street lamp nodes.</p>
</div>
<div id="comment-77392-info" class="comment-info">
<span class="comment-age">(04 Nov '20, 11:04)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-74345" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74345-form-container" class="comment-form-container">
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

<span id="74357"></span>

<div id="answer-container-74357" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74357-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-74357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OK, so I sat down and tried to get into the depths of Overpass Turbo style sheets. Not that difficult once you find out what to do in general. <em>(While the language guide is very extensive I always find it lacking some practical examples, but that is another story.)</em></p>
<p>This already does the job quite well for me. I might add more differentiation or filters later.</p>
<pre><code>[out:json][timeout:25];
// gather results
(
  way[highway]({{bbox}});
  node[highway=street_lamp]({{bbox}});
)
;
// print results
out body;
&gt;;
out skel qt;
&#10;{{style:
/* lamps */
node {symbol-size:5; color:orange;fill-color: yellow}
&#10;/* default for highways */
way[highway] {color:darkcyan; width:3; opacity:0.3; }
&#10;/* highways with lit tag */
way[lit] {color:orange; width:10; opacity:0.5; }
&#10;/* highways with specific lit tag */
way[lit=no] {color:black; opacity:0.5;}
  way[lit=yes] {color:yellow; opacity:0.5;}
}}</code></pre>
<p>Would there be a way of getting rid of the circles that OT draws when the objects are small? i don't really need them and they are quite distracting.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '20, 13:52</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Nov '20, 11:03</strong> </span></p>
</div>
</div>
<div id="comments-container-74357" class="comments-container">
<span id="74359"></span>
<div id="comment-74359" class="comment">
<div id="post-74359-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>you can find a setting under "Settings -&gt; Map -&gt; "Do not show small objects as POIs". Note that this is my translation of the Dutch text I see.</p>
</div>
<div id="comment-74359-info" class="comment-info">
<span class="comment-age">(25 Apr '20, 10:45)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-74357" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74357-form-container" class="comment-form-container">
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

