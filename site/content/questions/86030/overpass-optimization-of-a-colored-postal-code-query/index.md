+++
type = "question"
title = "Overpass: Optimization of a Colored Postal Code Query"
description = '''Hello, I hope you&#x27;re all doing well! First of all, unfortunately, my knowledge regarding javascript query building in Overpass is relatively limited. I would like to create a map of German postalcode areas that are colored differently. It can happen that several postal code areas should have the sam...'''
date = "2022-10-31T09:39:00Z"
lastmod = "2022-10-31T11:09:00Z"
weight = 86030
keywords = [ "overpass", "colors", "postal_code", "relations" ]
aliases = [ "/questions/86030" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass: Optimization of a Colored Postal Code Query](/questions/86030/overpass-optimization-of-a-colored-postal-code-query)

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
<span id="post-86030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86030-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I hope you're all doing well!</p>
<p>First of all, unfortunately, my knowledge regarding javascript query building in Overpass is relatively limited. I would like to create a map of German postalcode areas that are colored differently. It can happen that several postal code areas should have the same color. The following code is already functioning:</p>
<pre><code>[out:json][timeout:25];
&#10;{{geocodeArea:Germany}}-&gt;.searchArea;
&#10;// gather results
(      
  relation[&quot;postal_code&quot;=&quot;45529&quot;](area.searchArea);
  relation[&quot;postal_code&quot;=&quot;45527&quot;](area.searchArea);  
  relation[&quot;postal_code&quot;=&quot;45525&quot;](area.searchArea);
);
&#10;
{{style:
  relation[postal_code=45529]
    { color:red; fill-color:red; text: note;}
  relation[postal_code=45527]
    { color:red; fill-color:red; text: note;}
  relation[postal_code=45525]
    { color:yellow; fill-color:yellow; text: note;}
}}
&#10;// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>However, I'm pretty sure that there is room for improvement for shortening the code and, therefore, the URL link created from this query. Maybe it is possible to place several postal codes in one relation? Maybe the style code can be improved to merge the postal codes with the same color?</p>
<p>Thank you very much in advance!</p>
<p>All the best Josh</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-colors" rel="tag" title="see questions tagged &#39;colors&#39;">colors</span> <span class="post-tag tag-link-postal_code" rel="tag" title="see questions tagged &#39;postal_code&#39;">postal_code</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '22, 09:39</strong></p>
<img src="https://secure.gravatar.com/avatar/ac29216bdd809890cec35eb5f25afd35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joshua1511&#39;s gravatar image" />
<p><span>Joshua1511</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joshua1511 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86030" class="comments-container">
&#10;</div>
<div id="comment-tools-86030" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86030-form-container" class="comment-form-container">
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

<span id="86033"></span>

<div id="answer-container-86033" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86033-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>{{geocodeArea:Germany}};rel[postal_code~&quot;45529|45527|45525&quot;](area);{{style:relation{fill-color:red;text:note}relation[postal_code=45525]{fill-color:yellow} }}out geom;</code></pre>
<ul>
<li>Combine search for similar entities into one command.</li>
<li>Use <code>'rel'</code> instead of <code>relation</code></li>
<li>Remove unnecessary parenthesis</li>
<li>Remove timeout</li>
<li>Remove <code>out:json</code> if you're not interested in data format</li>
<li>use <code>out geom;</code> if you're not interested in data format</li>
<li>Remove whitespace</li>
<li>Remove all comments</li>
<li>Remove carriage returns so it's all on one line (note space is required between the style closing curly brackets)</li>
<li>Remove comma after '<code>note</code>' &amp; '<code>yellow</code>'</li>
<li>Is <code>color:</code> required?</li>
</ul>
<p>MapCss works on a default system so you can specify a colour for the relations you want red &amp; specify postal_codes for those with a different colour. If you want labels to display in all areas it only needs to be declared once.</p>
<p>In your specific example there's no requirement to search using the area as the postal_codes are unique, but that might no be true in every case.</p>
<p>In your specific example you could also reduce the search to <code>postal_code~"4552."</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '22, 11:02</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Oct '22, 11:03</strong> </span></p>
</div>
</div>
<div id="comments-container-86033" class="comments-container">
<span id="86034"></span>
<div id="comment-86034" class="comment">
<div id="post-86034-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is awesome! Thank you very much! I'll play a bit around with your code.</p>
</div>
<div id="comment-86034-info" class="comment-info">
<span class="comment-age">(31 Oct '22, 11:09)</span> <span class="comment-user userinfo">Joshua1511</span>
</div>
</div>
</div>
<div id="comment-tools-86033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86033-form-container" class="comment-form-container">
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

