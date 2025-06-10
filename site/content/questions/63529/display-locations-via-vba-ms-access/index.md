+++
type = "question"
title = "Display locations via VBA (MS Access)"
description = '''I have an example of how it works with Google Maps (see below). I want the map to be opened via OpenStreetMap. Can one of you rewrite the code? str = &quot;&amp;lt;iframe width=&quot;&quot; 425&quot;&quot;=&quot;&quot; height=&quot;&quot; 350&quot;&quot;=&quot;&quot; frameborder=&quot;&quot; 0&quot;&quot;=&quot;&quot; scrolling=&quot;&quot; no&quot;&quot;=&quot;&quot; marginheight=&quot;&quot; 0&quot;&quot;=&quot;&quot; marginwidth=&quot;&quot; 0&quot;&quot;=&quot;&quot; src=&quot;&quot; http:=...'''
date = "2018-05-17T10:25:00Z"
lastmod = "2018-05-17T11:15:00Z"
weight = 63529
keywords = [ "vba", "msaccess", "location" ]
aliases = [ "/questions/63529" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Display locations via VBA (MS Access)](/questions/63529/display-locations-via-vba-ms-access)

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
<span id="post-63529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63529-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have an example of how it works with Google Maps (see below). I want the map to be opened via OpenStreetMap. Can one of you rewrite the code?</p>
<p>str = "&lt;iframe width="" 425""="" height="" 350""="" frameborder="" 0""="" scrolling="" no""="" marginheight="" 0""="" marginwidth="" 0""="" src="" http:="" maps.google.de="" maps?f="q&amp;amp;source=s_q&amp;amp;hl=de&amp;amp;geocode=&amp;amp;q="" &amp;="" _="" strstrasse="" &amp;="" "="" "="" &amp;="" me!hausnummer="" &amp;="" "+"="" &amp;="" strort="" &amp;="" "+"="" &amp;="" me!plz="" &amp;="" "&amp;amp;sll=" &amp;amp; strK &amp;amp; " &amp;amp;sspn="0.098084,0.368647&amp;amp;ie=UTF8&amp;amp;hq=&amp;amp;hnear="" &amp;="" _="" strstrasse="" &amp;="" "="" "="" &amp;="" me!hausnummer="" &amp;="" ","="" &amp;="" me!plz="" &amp;="" "+"="" &amp;="" strort="" &amp;="" "&amp;amp;z=" &amp;amp; Me!Zoom &amp;amp; " &amp;amp;ll=" &amp;amp; strK &amp;amp; " &amp;amp;output="embed"""&gt;&lt;/iframe&gt;<br />
<span class="small">&lt;a"</span></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-vba" rel="tag" title="see questions tagged &#39;vba&#39;">vba</span> <span class="post-tag tag-link-msaccess" rel="tag" title="see questions tagged &#39;msaccess&#39;">msaccess</span> <span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 May '18, 10:25</strong></p>
<img src="https://secure.gravatar.com/avatar/eafe98b248d86b2e8b5f45e0b1325e93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="silosix&#39;s gravatar image" />
<p><span>silosix</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="silosix has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-63529" class="comments-container">
&#10;</div>
<div id="comment-tools-63529" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63529-form-container" class="comment-form-container">
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

<span id="63530"></span>

<div id="answer-container-63530" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63530-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at the embed share function on <a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> :</p>
<ul>
<li>Share button on the right of the screen</li>
<li>Click on HTML button</li>
<li>You'll have the code of the OpenStreetMap <code>iframe</code></li>
<li>You just have to replace your Google <code>iframe</code> by the OpenStreetMap one</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '18, 10:31</strong></p>
<img src="https://secure.gravatar.com/avatar/08e299a7143fc92767e9c66bff9481bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbelien&#39;s gravatar image" />
<p><span>jbelien</span><br />
<span class="score" title="146 reputation points">146</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbelien has one accepted answer">16%</span></p>
</div>
</div>
<div id="comments-container-63530" class="comments-container">
<span id="63531"></span>
<div id="comment-63531" class="comment">
<div id="post-63531-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I'll try it.</p>
</div>
<div id="comment-63531-info" class="comment-info">
<span class="comment-age">(17 May '18, 10:35)</span> <span class="comment-user userinfo">silosix</span>
</div>
</div>
<span id="63532"></span>
<div id="comment-63532" class="comment">
<div id="post-63532-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you're putting it inside str = "" as above then you'll also need to replace every " in the generated HTML from the above steps by ""</p>
<p>It isn't clear why the string in the question ends with &lt;a which seems to be an incomplete HTML tag - if that <em>is</em> important you might have to add that on the end as well.</p>
</div>
<div id="comment-63532-info" class="comment-info">
<span class="comment-age">(17 May '18, 11:15)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63530" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63530-form-container" class="comment-form-container">
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

