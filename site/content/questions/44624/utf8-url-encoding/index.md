+++
type = "question"
title = "UTF8 URL ENCODING"
description = '''Hi, I am calling a nominatim WS through a Java client using this piece of code: String urls = &quot;http://nominatim.openstreetmap.org/search?q= &quot; + URLEncoder.encode(addressString.trim(), &quot;UTF-8&quot;) + &quot;&amp;amp;format=json&amp;amp;polygon=1&amp;amp;addressdetails=1&quot;; URL url = new URL(urls);  HttpURLConnection uc = (...'''
date = "2015-08-05T09:49:00Z"
lastmod = "2015-08-05T10:37:00Z"
weight = 44624
keywords = [ "nominatim", "utf-8", "encoding" ]
aliases = [ "/questions/44624" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [UTF8 URL ENCODING](/questions/44624/utf8-url-encoding)

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
<span id="post-44624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44624-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am calling a nominatim WS through a Java client using this piece of code:</p>
<pre><code>String urls = &quot;http://nominatim.openstreetmap.org/search?q= &quot; + URLEncoder.encode(addressString.trim(), &quot;UTF-8&quot;) + &quot;&amp;format=json&amp;polygon=1&amp;addressdetails=1&quot;;
URL url = new URL(urls);            
HttpURLConnection uc = (HttpURLConnection) url.openConnection();            
uc.setRequestProperty(&quot;Accept-Charset:&quot;, &quot;UTF-8&quot;);
uc.setRequestProperty(&quot;Content-Type:&quot;,&quot;application/x-www-form-urlencoded;charset=utf-8&quot;);</code></pre>
<p>But i got this error:</p>
<pre><code>&#39;406: Not Acceptable&#39; for url: &#39;http://nominatim.openstreetmap.org/search?q= %CE%A0%CE%91%CE%A1%CE%99%CE%A3%CE%99&amp;format=json&amp;polygon=1&amp;addressdetails=1&#39;</code></pre>
<p>Thanks and best Regards,</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-utf-8" rel="tag" title="see questions tagged &#39;utf-8&#39;">utf-8</span> <span class="post-tag tag-link-encoding" rel="tag" title="see questions tagged &#39;encoding&#39;">encoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Aug '15, 09:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a0f95826dac7e3a0b7666f7bb0f22571?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ricard_3&#39;s gravatar image" />
<p><span>ricard_3</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ricard_3 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Aug '15, 10:36</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-44624" class="comments-container">
&#10;</div>
<div id="comment-tools-44624" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44624-form-container" class="comment-form-container">
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

<span id="44628"></span>

<div id="answer-container-44628" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44628-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>removing the white space after q "q= " has solved the problem. Thanks</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Aug '15, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a0f95826dac7e3a0b7666f7bb0f22571?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ricard_3&#39;s gravatar image" />
<p><span>ricard_3</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ricard_3 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44628" class="comments-container">
&#10;</div>
<div id="comment-tools-44628" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44628-form-container" class="comment-form-container">
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

