+++
type = "question"
title = "OsmLib Ruby Export KML Polygons"
description = '''I have been trying to figure out, is it possible to produce KML polygons from OSM areas with the OSMLib ruby? I have already made quite a few modifications to the ruby source to fit my needs, but I still can&#x27;t get this part to work.. In the osmlib-base-0.1.4/lib folder, in objects.rb, I added: ** Up...'''
date = "2011-02-22T06:35:00Z"
lastmod = "2011-02-22T16:05:00Z"
weight = 3250
keywords = [ "osmlib", "kml", "ruby", "area" ]
aliases = [ "/questions/3250" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OsmLib Ruby Export KML Polygons](/questions/3250/osmlib-ruby-export-kml-polygons)

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
<span id="post-3250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3250-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been trying to figure out, is it possible to produce KML polygons from OSM areas with the OSMLib ruby? I have already made quite a few modifications to the ruby source to fit my needs, but I still can't get this part to work..</p>
<p>In the osmlib-base-0.1.4/lib folder, in objects.rb, I added: ** Updated code below</p>
<pre><code>        if (tags[&#39;area&#39;] == &#39;yes&#39; &amp;&amp; is_closed?)
          polygon 
        else
          linestring
        end</code></pre>
<p>Replacing what was previously just:</p>
<pre><code>    def geometry
        linestring
    end</code></pre>
<p>That didn't seem to do the trick (there is already some geometry polygon code in the KML output, but obviously not enough! I don't know much at all about Ruby (this project is the first time I have used ruby at all!). Anyone have some tips/want to help implement this? I am sure this could get implemented properly and would be of use to people.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmlib" rel="tag" title="see questions tagged &#39;osmlib&#39;">osmlib</span> <span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span> <span class="post-tag tag-link-ruby" rel="tag" title="see questions tagged &#39;ruby&#39;">ruby</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Feb '11, 06:35</strong></p>
<img src="https://secure.gravatar.com/avatar/3a5c89275037ff2627640835b33e9483?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbski&#39;s gravatar image" />
<p><span>wbski</span><br />
<span class="score" title="146 reputation points">146</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbski has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Feb '11, 16:03</strong> </span></p>
</div>
</div>
<div id="comments-container-3250" class="comments-container">
&#10;</div>
<div id="comment-tools-3250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3250-form-container" class="comment-form-container">
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

<span id="3256"></span>

<div id="answer-container-3256" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3256-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Firstly, your approach will mistakenly put many objects in the polygon category, e.g. a highway roundabout; these are not, as your code seems to assume, tagged "area=no". To do this right you would have to look at the specific tags (i.e. closed way tagged as forest =&gt; polygon; closed way tagged as fence =&gt; linestring etc.)</p>
<p>Secondly, are you sure that the areas you hope to see on output are closed ways at all - or are they maybe multipolygon relation, in which case you would need a totally different approach?</p>
<p>You might want to look at <a href="http://blog.jochentopf.com/2011-01-05-osmium.html">Osmium/Osmjs</a>, by the same author, a program that lets you execute arbitrary Javascript code for OSM objects (you would still have to write the KML output part though). This program has good support for multipolygons.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '11, 07:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-3256" class="comments-container">
<span id="3258"></span>
<div id="comment-3258" class="comment">
<div id="post-3258-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... thirdly, you need to refactor your code, since even if the if condition matches, the function will return the results of the last computation, which as written above is always linestring.</p>
</div>
<div id="comment-3258-info" class="comment-info">
<span class="comment-age">(22 Feb '11, 09:47)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="3276"></span>
<div id="comment-3276" class="comment">
<div id="post-3276-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I see what you mean Frederik about not handling all the polygons properly.. However, in my application (ski runs), determining the areas is pretty simple, I will change tagging to area==yes. Anyways, I can tweak the logic to select forests etc later. I changed my code above, but still not working..</p>
<p>Now getting: geo_ruby/simple_features/polygon.rb:17:in <code>send': undefined method</code>points' for #&lt;array:0x1022a3840&gt; (NoMethodError)</p>
<p>Its a mystery to me..</p>
</div>
<div id="comment-3276-info" class="comment-info">
<span class="comment-age">(22 Feb '11, 16:05)</span> <span class="comment-user userinfo">wbski</span>
</div>
</div>
</div>
<div id="comment-tools-3256" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3256-form-container" class="comment-form-container">
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

