+++
type = "question"
title = "Overpass: get values with &quot;special&quot; characters"
description = '''Hello I am trying to use a query for retrieving wrong ( abbreviated ) values in keys, for example: places of worship which names beginning with &quot;S.&quot; this is the query [out:xml] ; (  node  [&quot;name&quot;~&quot;^S&#92;.&quot;]  [&quot;amenity&quot;=&quot;place_of_worship&quot;]  (46.00,12.24,46.70,13.80);  way  [&quot;name&quot;~&quot;^S&#92;.&quot;]  [&quot;amenity&quot;=&quot;p...'''
date = "2013-02-16T17:53:00Z"
lastmod = "2013-02-19T22:11:00Z"
weight = 19987
keywords = [ "regex", "overpass", "character" ]
aliases = [ "/questions/19987" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass: get values with "special" characters](/questions/19987/overpass-get-values-with-special-characters)

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
<span id="post-19987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19987-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello</p>
<p>I am trying to use a query for retrieving wrong ( abbreviated ) values in keys, for example: places of worship which names beginning with "S."</p>
<p>this is the query</p>
<pre><code>[out:xml]
;
(
  node
    [&quot;name&quot;~&quot;^S\.&quot;]
    [&quot;amenity&quot;=&quot;place_of_worship&quot;]
    (46.00,12.24,46.70,13.80);
  way
    [&quot;name&quot;~&quot;^S\.&quot;]
    [&quot;amenity&quot;=&quot;place_of_worship&quot;]
    (46.00,12.24,46.70,13.80); 
);
out meta;
&gt;;
out meta;</code></pre>
<p>This returns ALL the features beginning whith "S", backslash before the dot seems not to work.</p>
<p>Where am I wrong?</p>
<p>Thank You</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-regex" rel="tag" title="see questions tagged &#39;regex&#39;">regex</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-character" rel="tag" title="see questions tagged &#39;character&#39;">character</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '13, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/1ac18e3a979dc68dbb2c0b4ab7693ddc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gpstracks&#39;s gravatar image" />
<p><span>gpstracks</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gpstracks has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19987" class="comments-container">
&#10;</div>
<div id="comment-tools-19987" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19987-form-container" class="comment-form-container">
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

<span id="20010"></span>

<div id="answer-container-20010" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20010-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-20010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In Overpass QL you need to escape backslashes: ["name"~"^S\."] results in the regular expression ^S. (which finds every name starting with "S"). By contrast, ["name"~"^S\\."] produces the most likely ment regular expression ^S\. (which finds every name starting with "S.").</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '13, 08:23</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-20010" class="comments-container">
<span id="20050"></span>
<div id="comment-20050" class="comment">
<div id="post-20050-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It works. Thank You</p>
</div>
<div id="comment-20050-info" class="comment-info">
<span class="comment-age">(19 Feb '13, 22:11)</span> <span class="comment-user userinfo">gpstracks</span>
</div>
</div>
</div>
<div id="comment-tools-20010" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20010-form-container" class="comment-form-container">
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

