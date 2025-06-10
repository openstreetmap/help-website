+++
type = "question"
title = "quotes in Overpass Turbo style"
description = '''I was just trying to style an Overpass Turbo result by highlighting all buildings that contain a buildings:levels tag. I tried a query along: [out:json][timeout:25]; // gather results (  nwr[building]({{bbox}});  nwr[building][&quot;building:levels&quot;]({{bbox}}); ); // print results out body; &amp;gt;; out ske...'''
date = "2020-09-02T08:44:00Z"
lastmod = "2020-09-02T10:30:00Z"
weight = 76403
keywords = [ "quotes", "style", "overpass-turbo" ]
aliases = [ "/questions/76403" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [quotes in Overpass Turbo style](/questions/76403/quotes-in-overpass-turbo-style)

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
<span id="post-76403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76403-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was just trying to style an Overpass Turbo result by highlighting all buildings that contain a <code>buildings:levels</code> tag. I tried a query along:</p>
<pre><code>[out:json][timeout:25];
// gather results
(
  nwr[building]({{bbox}});
  nwr[building][&quot;building:levels&quot;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;
&#10;{{style:
  node, way, relation {color:green;}
  node[&quot;building:levels&quot;], way[&quot;building:levels&quot;], relation[&quot;building:levels&quot;]{color:red;}
}}</code></pre>
<p>According to <a href="https://wiki.openstreetmap.org/wiki/MapCSS/0.2">our wiki in MapCSS</a> tags containing other characters than letters and underscore should be enclosed in quotes. When I try to run above query, though, Overpass Turbo says the style definition got an error.</p>
<p>Is there a way to style non-letter tags in Overpass Turbo?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-quotes" rel="tag" title="see questions tagged &#39;quotes&#39;">quotes</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '20, 08:44</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-76403" class="comments-container">
<span id="76409"></span>
<div id="comment-76409" class="comment">
<div id="post-76409-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For the avoidance of doubt - the language used by Overpass Turbo and MapCSS are two completely different things.</p>
</div>
<div id="comment-76409-info" class="comment-info">
<span class="comment-age">(02 Sep '20, 10:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="76410"></span>
<div id="comment-76410" class="comment">
<div id="post-76410-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not according to Overpass Turbo itself. In its help section it epxlicitly refers to MapCSS and links to the wiki page <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo/MapCSS.">https://wiki.openstreetmap.org/wiki/Overpass_turbo/MapCSS.</a> That page in turn refers to the general MapCSS wiki page: <a href="https://wiki.openstreetmap.org/wiki/MapCSS">https://wiki.openstreetmap.org/wiki/MapCSS</a></p>
</div>
<div id="comment-76410-info" class="comment-info">
<span class="comment-age">(02 Sep '20, 10:30)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-76403" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76403-form-container" class="comment-form-container">
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

<span id="76405"></span>

<div id="answer-container-76405" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76405-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TZorn has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Removing the quotes completely for the style definition works for me:</p>
<pre><code>[out:json][timeout:25];
// gather results
(
  nwr[building]({{bbox}});
  nwr[building][&quot;building:levels&quot;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;
&#10;{{style:
  node, way, relation {color:green;}
  node[building:levels], way[building:levels], relation[building:levels]{color:red;}
}}</code></pre>
<p>According to the documentation this is not allowed, though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '20, 09:19</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-76405" class="comments-container">
<span id="76406"></span>
<div id="comment-76406" class="comment">
<div id="post-76406-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm probably never going to use a query like this but would someone please take the time to correct the documentation.</p>
<p>Many thanks,</p>
</div>
<div id="comment-76406-info" class="comment-info">
<span class="comment-age">(02 Sep '20, 10:07)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="76408"></span>
<div id="comment-76408" class="comment">
<div id="post-76408-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'll be damned. I'm pretty sure I had tried that already. But you are right, it does work.</p>
</div>
<div id="comment-76408-info" class="comment-info">
<span class="comment-age">(02 Sep '20, 10:24)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-76405" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76405-form-container" class="comment-form-container">
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

