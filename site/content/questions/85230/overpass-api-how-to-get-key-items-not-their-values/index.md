+++
type = "question"
title = "Overpass API: How to get key items (not their values)"
description = '''Hello, Struggling to do this Overpass query, ready to give up so I ask just in case it is possible! Heads up, I am just a hobbyist starting up so I can follow some code extracts and try to understand them but it&#x27;s quite hard for me to come up with my own code. I work on this node for example and I c...'''
date = "2022-07-26T22:10:00Z"
lastmod = "2022-07-26T22:10:00Z"
weight = 85230
keywords = [ "keys", "overpass-turbo" ]
aliases = [ "/questions/85230" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: How to get key items (not their values)](/questions/85230/overpass-api-how-to-get-key-items-not-their-values)

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
<span id="post-85230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85230-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>Struggling to do this Overpass query, ready to give up so I ask just in case it is possible! Heads up, I am just a hobbyist starting up so I can follow some code extracts and try to understand them but it's quite hard for me to come up with my own code.</p>
<p>I work on this <a href="https://www.openstreetmap.org/node/9269458264">node</a> for example and I can display the bin and show the name in a box using css. No problem so far...</p>
<pre><code>[out:json];
(
  node[&quot;amenity&quot;=&quot;recycling&quot;]({{bbox}});
);
out body;
&gt;;
out skel qt;
{{style:
  node[amenity=recycling] {
    icon-image: url(&#39;icons/maki/waste-basket-24@2x.png&#39;);
    icon-width: 30;
    text:name;
  }
}}</code></pre>
<p>Now, 2nd step, I want replace the name in the box by what kind of recycling it offers (clothes, glass_bottles, paper, etc...).</p>
<p>So I am not interested in the value of these keys but the actual keys themselves. Is there any way to do this using Overpass Turbo?</p>
<p>Any help very much appreciated.</p>
<p>Cheers!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-keys" rel="tag" title="see questions tagged &#39;keys&#39;">keys</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jul '22, 22:10</strong></p>
<img src="https://secure.gravatar.com/avatar/271af5e032a6a57ee36c09abd7b40d4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SterylMreep&#39;s gravatar image" />
<p><span>SterylMreep</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SterylMreep has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85230" class="comments-container">
&#10;</div>
<div id="comment-tools-85230" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85230-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

