+++
type = "question"
title = "disrupted postcode areas"
description = '''I try to map a disrupted postcode area to an area that also matches landuse=&quot;residential&quot;. I thought I&#x27;d use the German approach with multipolygon ... The village lies in Luxemburg near the German border. I couldn&#x27;t find any advice on how the Luxemburgish mapping community addresses postal_code, but...'''
date = "2013-08-25T20:30:00Z"
lastmod = "2013-08-28T16:27:00Z"
weight = 25780
keywords = [ "postcode", "multipolygon" ]
aliases = [ "/questions/25780" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [disrupted postcode areas](/questions/25780/disrupted-postcode-areas)

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
<span id="post-25780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25780-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I try to map a disrupted postcode area to an area that also matches landuse="residential". I thought I'd use the <a href="https://wiki.openstreetmap.org/wiki/Import/Catalogue/Postleitzahlen_Deutschland_2010">German approach with multipolygon</a> ...</p>
<p>The village lies in Luxemburg near the German border. I couldn't find any advice on how the Luxemburgish mapping community addresses postal_code, but Nomanitim doesn't return any result for Luxemburgish Postcodes so far, although the mappers applied postal_code to streets directly (never saw that before). So I think it should be solved differently.</p>
<p>I try to describe it in a very simple way: suppose we have 2 postcodes A and B in village X.</p>
<p>They are "stacked" like this, with A being the old center of the village</p>
<pre><code>B
 A
B</code></pre>
<p>BAB prefectly matches the landuse="residential" area.</p>
<p><img src="/upfiles/disrupted-postcode-areas.png" alt="disrupted postcode area" /></p>
<p>Is it OK to have at the end 3 mutlipolygons sharing the common ways, all components specified as "outer"?</p>
<ol>
<li>village X</li>
<li>postocde area A</li>
<li>postcode area B made up of 1 single multipolygon, but defining 2 closed areas</li>
</ol>
<p>Thanks for your advice, Georges</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '13, 20:30</strong></p>
<img src="https://secure.gravatar.com/avatar/01f034fda5a86c909eb97506c7c4284b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gjesch&#39;s gravatar image" />
<p><span>gjesch</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gjesch has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Aug '13, 21:08</strong> </span></p>
</div>
</div>
<div id="comments-container-25780" class="comments-container">
&#10;</div>
<div id="comment-tools-25780" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25780-form-container" class="comment-form-container">
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

<span id="25823"></span>

<div id="answer-container-25823" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25823-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, you solution sounds good!</p>
<p>There are a bunch of such separated areas with the same postal_code in Germany, too.</p>
<p>If you have done your edit, give us a permalink to that town, then we can inspect the relations.</p>
<p>There are also some ways to visualize boundary areas mapped as relations, there you can even detect logical errors in boundary elements.</p>
<p>More to come ...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Aug '13, 16:39</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-25823" class="comments-container">
<span id="25831"></span>
<div id="comment-25831" class="comment">
<div id="post-25831-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was almost sure that my approach must be OK, so I uploaded the data already yesterday. And Nomanitim shows exactly the result I was expecting (hoping) to see with "lenningen 5431". "5430" is the other postcode.</p>
<p><a href="https://www.openstreetmap.org/?relation=3163883#map=16/49.6011/6.3658">https://www.openstreetmap.org/?relation=3163883#map=16/49.6011/6.3658</a></p>
<p>But to which extend is this applicable? I had already to guide one border through connected buildings (left near the church). But there is apparently another building in the north of the village lying in a second row of postcode 5431 but belonging to 5430. Should I really draw an island area with role=inner for multipolygon 5431 and role=outer for multiploygon 5430. Isn't that overkill for one building?</p>
<p>In Luxemburg you have 4 digits postcodes with round about 500 localities. You can imagine that often a postcode only covers a couple of streets. Sometimes you can barely call them areas. If you have just 2-5 streets covered by a postcode, a simple postcode relation tying these streets together would be much simpler.</p>
<p>But I'm afraid of the many different algorithms client software have to provide to analyze all the concurrent strategies to organize hierarchical data.</p>
</div>
<div id="comment-25831-info" class="comment-info">
<span class="comment-age">(26 Aug '13, 21:55)</span> <span class="comment-user userinfo">gjesch</span>
</div>
</div>
<span id="25901"></span>
<div id="comment-25901" class="comment">
<div id="post-25901-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmmm, comparing to postal_code system in Germany, maybe it is too easy to draw a boundary around a bunch of streets and houses, and to define by this "little" area that this the area with postal_code=xxxx</p>
<p>Only for a general compare: is there an official map online where we can see the system of postal_code areas in Luxembourg?</p>
<p>If you can speak German a little bit, then I invite you to the german section at <a href="http://forum.openstreetmap.org">http://forum.openstreetmap.org</a> ... there we have a quite recent topic about the correctness of postal_code areas in Germany.</p>
</div>
<div id="comment-25901-info" class="comment-info">
<span class="comment-age">(28 Aug '13, 16:27)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-25823" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25823-form-container" class="comment-form-container">
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

