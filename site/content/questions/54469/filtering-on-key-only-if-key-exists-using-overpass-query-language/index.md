+++
type = "question"
title = "Filtering on key only if key exists using overpass query language"
description = '''I want to match bridges which are considered metallic or unknown. I tried this: area[name=&quot;Australia&quot;]-&amp;gt;.a; way(area.a) [man_made=bridge] [bridge!=viaduct] [&quot;bridge:structure&quot;!=humpback] [material~metal] [material~steel] [material~reinforced_concrete] [&quot;bridge:material&quot;~steel] [&quot;bridge:material&quot;~...'''
date = "2017-02-05T09:46:00Z"
lastmod = "2017-02-05T11:22:00Z"
weight = 54469
keywords = [ "overpass", "overpass-ql" ]
aliases = [ "/questions/54469" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering on key only if key exists using overpass query language](/questions/54469/filtering-on-key-only-if-key-exists-using-overpass-query-language)

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
<span id="post-54469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54469-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to match bridges which are considered metallic or unknown.</p>
<p>I tried this:</p>
<pre><code>area[name=&quot;Australia&quot;]-&gt;.a;
way(area.a)
[man_made=bridge]
[bridge!=viaduct]
[&quot;bridge:structure&quot;!=humpback]
[material~metal]
[material~steel]
[material~reinforced_concrete]
[&quot;bridge:material&quot;~steel]
[&quot;bridge:material&quot;~metal];
out geom;</code></pre>
<p>But it this ignores bridges that don't have the material or "bridge:material" key. Looking at the overpass docs doesn't mention anyway to match on a key only if that key exists.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '17, 09:46</strong></p>
<img src="https://secure.gravatar.com/avatar/e853191a066217d7b8fe16608c757506?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CMCDragonkai&#39;s gravatar image" />
<p><span>CMCDragonkai</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CMCDragonkai has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54469" class="comments-container">
<span id="54473"></span>
<div id="comment-54473" class="comment">
<div id="post-54473-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think you should use the union operator ( ) and search for bridges without bridge:material on one hand with [!"bridge:material"] and the ones you are looking for above.</p>
</div>
<div id="comment-54473-info" class="comment-info">
<span class="comment-age">(05 Feb '17, 11:22)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-54469" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54469-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

