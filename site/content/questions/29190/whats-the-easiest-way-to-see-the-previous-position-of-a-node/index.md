+++
type = "question"
title = "What&#x27;s the easiest way to see the previous position of a node?"
description = '''I recently moved this node to a new location. What&#x27;s the easiest way to show it on a map, and a marker where the previous location was?'''
date = "2013-12-19T10:40:00Z"
lastmod = "2013-12-19T16:53:00Z"
weight = 29190
keywords = [ "location", "history" ]
aliases = [ "/questions/29190" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [What's the easiest way to see the previous position of a node?](/questions/29190/whats-the-easiest-way-to-see-the-previous-position-of-a-node)

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
<span id="post-29190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29190-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-29190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently moved <a href="http://www.openstreetmap.org/node/1784789012/history">this node</a> to a new location. What's the easiest way to show it on a map, and a marker where the previous location was?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Dec '13, 10:40</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-29190" class="comments-container">
<span id="29195"></span>
<div id="comment-29195" class="comment">
<div id="post-29195-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to understand you correctly, you want to view both the previous position and the new one?</p>
</div>
<div id="comment-29195-info" class="comment-info">
<span class="comment-age">(19 Dec '13, 12:51)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-29190" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29190-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="29192"></span>

<div id="answer-container-29192" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29192-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-29192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Currently, you don't have an "easy way" like in 2 mouse clicks to do this. But...</p>
<p>Here is one method I found:</p>
<p>- from the <a href="http://www.openstreetmap.org/node/1784789012/history">node history</a>, you can copy the previous coordinates (in version 1 : "53.5999303, -1.0152212")<br />
- click the button "share" and copy the "link" field <a href="http://www.openstreetmap.org/#map=19/53.59996/-1.01558">http://www.openstreetmap.org/#map=19/53.59996/-1.01558</a> into your browser<br />
- edit the URL and replace the older coordinates by the ones you got from the node history version 1 : "mlat=53.59993&amp;mlon=-1.01522#map=19/53.5999303/-1.0152212" .(the "mlat" and "mlon" define the marker position and "#map" the slippy map central position)<br />
- You get <a href="http://www.openstreetmap.org/?mlat=53.59993&amp;mlon=-1.01522#map=19/53.59993/-1.01522">this result</a>.</p>
<p>That's it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '13, 12:12</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Dec '13, 12:33</strong> </span></p>
</div>
</div>
<div id="comments-container-29192" class="comments-container">
<span id="29194"></span>
<div id="comment-29194" class="comment">
<div id="post-29194-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Instead of editing the URL you can just copy'n'paste the coordinates into the search field and click on the first result. The marker will be added automatically. Note: This doesn't work for every locale. Some translations (e.g. german) display the coordinates using commas as decimal points (e.g. <em>-1,01</em> instead of <em>-1.01</em>) which have to be replaced first.</p>
</div>
<div id="comment-29194-info" class="comment-info">
<span class="comment-age">(19 Dec '13, 12:46)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="29196"></span>
<div id="comment-29196" class="comment">
<div id="post-29196-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good try but the problem with this method is that the marker disappears when you close the search pan :( I didn't find a way to create an URL with the marker from the "find" tool.</p>
</div>
<div id="comment-29196-info" class="comment-info">
<span class="comment-age">(19 Dec '13, 12:57)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="29197"></span>
<div id="comment-29197" class="comment">
<div id="post-29197-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I just opened a <a href="https://github.com/openstreetmap/openstreetmap-website/issues/663">ticket</a> suggesting to add the marker automatically to the 'Location:' links of node histories.</p>
</div>
<div id="comment-29197-info" class="comment-info">
<span class="comment-age">(19 Dec '13, 12:58)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-29192" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29192-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29200"></span>

<div id="answer-container-29200" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29200-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Similar to Pieren's solution but a bit easier:</p>
<ol>
<li>do for all location links:
<ol>
<li>(on the <a href="http://www.openstreetmap.org/node/1784789012/history">history page</a>) right click one of the location links (e.g. <a href="http://www.openstreetmap.org/?lat=53.5999607&amp;lon=-1.0152429&amp;zoom=18">http://www.openstreetmap.org/?lat=53.5999607&amp;lon=-1.0152429&amp;zoom=18</a> )</li>
<li>open a new tab</li>
<li>paste the URL (do <em>not</em> open yet)</li>
<li>edit the URL: insert two "m" (before lat and lon) (e.g. <a href="http://www.openstreetmap.org/?mlat=53.5999607&amp;mlon=-1.0152429&amp;zoom=18">http://www.openstreetmap.org/?mlat=53.5999607&amp;mlon=-1.0152429&amp;zoom=18</a> )</li>
<li>open this URL</li>
</ol></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '13, 15:53</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span> </br></p>
</div>
</div>
<div id="comments-container-29200" class="comments-container">
&#10;</div>
<div id="comment-tools-29200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29200-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29201"></span>

<div id="answer-container-29201" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29201-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>more easy to use (but somehow hard to set up): use this JavaScript snippet (similar to the one in <a href="https://trac.openstreetmap.org/ticket/5045#comment:9">my comment over there</a>). It converts all links to contain a "m" automatically. You can then open those links in new tabs to see the markers.</p>
<pre><code>if (document.location.href.split(&#39;#&#39;)[0].split(&#39;/&#39;).length &gt; 4) {
   if (document.location.href.split(&#39;#&#39;)[0].split(&#39;/&#39;)[3] === &#39;node&#39;) {
      $(&quot;div#sidebar_content div.geo a&quot;).each(function () {
                  $(this).attr(&quot;href&quot;, $(this).attr(&quot;href&quot;).replace(/([?&amp;])lat=/, &quot;$1mlat=&quot;).replace(/([?&amp;])lon=/, &quot;$1mlon=&quot;));
      });
   }
}</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '13, 16:53</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Dec '13, 19:25</strong> </span></p>
</div>
</div>
<div id="comments-container-29201" class="comments-container">
&#10;</div>
<div id="comment-tools-29201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29201-form-container" class="comment-form-container">
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

