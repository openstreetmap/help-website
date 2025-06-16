+++
type = "question"
title = "Internet explorer fails calling nominatim"
description = '''hello, i got a problem similar to https://help.openstreetmap.org/questions/722/why-does-nominatim-return-an-error-for-queries-from-internet-explorer that is my call to nominatim: Suche Flughafen Hamburg in Firefox i can read the answer in standard tab. In InternetExplorer i also receive the same res...'''
date = "2012-12-19T15:43:00Z"
lastmod = "2012-12-19T16:00:00Z"
weight = 18622
keywords = [ "jquery", "nominatim", "explorer", "internet" ]
aliases = [ "/questions/18622" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Internet explorer fails calling nominatim](/questions/18622/internet-explorer-fails-calling-nominatim)

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
<span id="post-18622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18622-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello,</p>
<p>i got a problem similar to <a href="/questions/722/why-does-nominatim-return-an-error-for-queries-from-internet-explorer">https://help.openstreetmap.org/questions/722/why-does-nominatim-return-an-error-for-queries-from-internet-explorer</a></p>
<p>that is my call to nominatim: <a href="http://nominatim.openstreetmap.org/search?q=flughafen%2Chamburg%2CDE&amp;format=json&amp;addressdetails=0&amp;limit=1">Suche Flughafen Hamburg</a> in Firefox i can read the answer in standard tab. In InternetExplorer i also receive the same result (after having a detail look with a debug tool)<br />
</p>
<p>But calling that link inside a webpage wih jquery... in Firefox anything is fine.</p>
<pre><code>  $.ajax({
      url: url,
      type : &quot;GET&quot;,
      success: function(result){
         alert(&quot;success&quot;);
      },
      error: function(err) {
        alert(&quot;error&quot;);
    } 
&#10;  });</code></pre>
<p>Using the internet explorer debugger the code runs to the error section. Without giving me useful information. it feels the URL isnt called.</p>
<p>Any ideas, what the problem is?</p>
<p>am using jquery-1.7.2 and jquery-ui-1.8.22</p>
<p>thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-jquery" rel="tag" title="see questions tagged &#39;jquery&#39;">jquery</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-explorer" rel="tag" title="see questions tagged &#39;explorer&#39;">explorer</span> <span class="post-tag tag-link-internet" rel="tag" title="see questions tagged &#39;internet&#39;">internet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Dec '12, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/c0bf0d071d7d51bc95640f09cc4e7e0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cortadillo&#39;s gravatar image" />
<p><span>Cortadillo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cortadillo has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-18622" class="comments-container">
<span id="18625"></span>
<div id="comment-18625" class="comment">
<div id="post-18625-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would suggest that using InternetExplorer is the problem. ;-) ... it was in the question you've linked to.</p>
</div>
<div id="comment-18625-info" class="comment-info">
<span class="comment-age">(19 Dec '12, 16:00)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-18622" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18622-form-container" class="comment-form-container">
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

<span id="18624"></span>

<div id="answer-container-18624" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18624-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have you checked your encoding as suggested in the question you linked to? Try searching for something without any special characters in it like 'london' and see if that works. If it does it would suggest an encoding problem - follow the advice from <a href="/questions/722/why-does-nominatim-return-an-error-for-queries-from-internet-explorer">https://help.openstreetmap.org/questions/722/why-does-nominatim-return-an-error-for-queries-from-internet-explorer</a>.</p>
<p>Alternatively can you try using format=jsonv2 instead. The v2 format was introduced to fix a problem with a conflict between the property 'class' used in the original json format.</p>
<p><a href="http://nominatim.openstreetmap.org/search?q=flughafen%2Chamburg%2CDE&amp;format=jsonv2&amp;addressdetails=0&amp;limit=1">http://nominatim.openstreetmap.org/search?q=flughafen%2Chamburg%2CDE&amp;format=jsonv2&amp;addressdetails=0&amp;limit=1</a></p>
<p>If neither of these are the cause you will need to use the debugger to view the actual response comming back from the nominatim server. You could also try replacing <code>alert("error");</code> with <code>alert(err);</code> to hopefully get some useful information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '12, 15:57</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Dec '12, 16:01</strong> </span></p>
</div>
</div>
<div id="comments-container-18624" class="comments-container">
&#10;</div>
<div id="comment-tools-18624" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18624-form-container" class="comment-form-container">
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

