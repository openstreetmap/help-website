+++
type = "question"
title = "Extract statistics for a city"
description = '''I want only to extract the statistics, like the number of POI`s, buildings, for a specific city from a weekly planet dump, or somewhere. So i can show to the users of that city, Bucharest in my example, how the map is evolving from week to week, and make a interactive chart'''
date = "2012-09-02T13:15:00Z"
lastmod = "2014-06-16T18:57:00Z"
weight = 15748
keywords = [ "statistics", "extract" ]
aliases = [ "/questions/15748" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Extract statistics for a city](/questions/15748/extract-statistics-for-a-city)

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
<span id="post-15748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15748-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want only to extract the statistics, like the number of POI`s, buildings, for a specific city from a weekly planet dump, or somewhere.</p>
<p>So i can show to the users of that city, Bucharest in my example, how the map is evolving from week to week, and make a interactive chart</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '12, 13:15</strong></p>
<img src="https://secure.gravatar.com/avatar/92a51d3af99ee124bb9e06dd35249910?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Badita%20Florin&#39;s gravatar image" />
<p><span>Badita Florin</span><br />
<span class="score" title="112 reputation points">112</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Badita Florin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15748" class="comments-container">
<span id="15750"></span>
<div id="comment-15750" class="comment">
<div id="post-15750-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I see that in nominatim you can select like this.</p>
<p>Maybe this would help in a way</p>
<p><a href="http://nominatim.openstreetmap.org/details.php?place_id=34846811">http://nominatim.openstreetmap.org/details.php?place_id=34846811</a></p>
</div>
<div id="comment-15750-info" class="comment-info">
<span class="comment-age">(02 Sep '12, 13:25)</span> <span class="comment-user userinfo">Badita Florin</span>
</div>
</div>
</div>
<div id="comment-tools-15748" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15748-form-container" class="comment-form-container">
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

<span id="15763"></span>

<div id="answer-container-15763" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15763-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-15763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Badita Florin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If it is a small area you can use <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> to directly get all POIs you are interested in inside a given bounding box.</p>
<p>Please type</p>
<pre><code>&lt;union&gt;
  &lt;area-query ref=&quot;3600377733&quot;/&gt;
  &lt;recurse type=&quot;up&quot;/&gt;
&lt;/union&gt;
&lt;print/&gt;</code></pre>
<p>into <a href="http://overpass-api.de/query_form.html">http://overpass-api.de/query_form.html</a>.</p>
<p>This gives you exactly the OSM elements within the city border of Bucharest.</p>
<p>For a larger area consider using a <a href="http://wiki.openstreetmap.org/wiki/Extract#Country_and_area_extracts">planet extract</a>. Afterwards you could use a combination of <a href="http://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a> and <a href="http://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a> to filter out the interesting data and finally do you calculations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '12, 18:19</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Sep '12, 07:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span></p>
</div>
</div>
<div id="comments-container-15763" class="comments-container">
<span id="15771"></span>
<div id="comment-15771" class="comment">
<div id="post-15771-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Given that a PBF for the whole of Romania is only 71Mb, I'd suggest that Overpass is the way to go.</p>
</div>
<div id="comment-15771-info" class="comment-info">
<span class="comment-age">(03 Sep '12, 22:03)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="16084"></span>
<div id="comment-16084" class="comment">
<div id="post-16084-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much, i did this and get a 21 mb file called</p>
<p>interpreter</p>
<p>Without a extension</p>
<p>I will google for what to to with this or if i did something wrong</p>
</div>
<div id="comment-16084-info" class="comment-info">
<span class="comment-age">(14 Sep '12, 14:14)</span> <span class="comment-user userinfo">Badita Florin</span>
</div>
</div>
<span id="16097"></span>
<div id="comment-16097" class="comment">
<div id="post-16097-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>On the "save" dialog it will probably have said what it was - an XML file (at least, that's what Firefox told me).</p>
<p>To see how many buildings are in there you can do something like:</p>
<pre><code>grep &#39;k=&quot;building&quot;&#39; interpreter | wc
   14425    43281   462468</code></pre>
<p>Similarly for other tags and values.</p>
<p>If you're on Windows and don't have GNU Utilities such as "grep" there try <a href="http://unxutils.sourceforge.net/">this</a>.</p>
</div>
<div id="comment-16097-info" class="comment-info">
<span class="comment-age">(14 Sep '12, 16:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="34010"></span>
<div id="comment-34010" class="comment">
<div id="post-34010-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Btw: 3600377733 = 3600000000 + ID of the Bucharest relation <a href="http://www.openstreetmap.org/relation/377733">http://www.openstreetmap.org/relation/377733</a></p>
</div>
<div id="comment-34010-info" class="comment-info">
<span class="comment-age">(16 Jun '14, 18:57)</span> <span class="comment-user userinfo">simon04</span>
</div>
</div>
</div>
<div id="comment-tools-15763" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15763-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15752"></span>

<div id="answer-container-15752" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15752-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not an expert about that, but you should try to import the raw weekly or daily diffed planet data into a <a href="http://wiki.openstreetmap.org/wiki/Databases_and_data_access_APIs">database</a> and then do a database query about special elements.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '12, 19:25</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-15752" class="comments-container">
&#10;</div>
<div id="comment-tools-15752" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15752-form-container" class="comment-form-container">
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

