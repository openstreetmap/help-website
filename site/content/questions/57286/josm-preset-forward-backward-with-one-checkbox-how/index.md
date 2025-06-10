+++
type = "question"
title = "JOSM preset, forward backward with one checkbox. How?"
description = '''We have a traffic_sign C12.  Because this sign works from one side. Their could be no sign on the other side. Other side, it is possible to enter and turn on road or visit a house/field. And go back. The way must set to forward or backward on a small section. Where you do not turn anymore. For the t...'''
date = "2017-07-26T14:48:00Z"
lastmod = "2017-07-30T20:49:00Z"
weight = 57286
keywords = [ "forward", "josm", "presets", "backward" ]
aliases = [ "/questions/57286" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM preset, forward backward with one checkbox. How?](/questions/57286/josm-preset-forward-backward-with-one-checkbox-how)

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
<span id="post-57286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57286-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We have a traffic_sign C12.</p>
<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Nederlands_verkeersbord_C12.svg/60px-Nederlands_verkeersbord_C12.svg.png" alt="alt text" /></p>
<p>Because this sign works from one side. Their could be no sign on the other side. Other side, it is possible to enter and turn on road or visit a house/field. And go back. The way must set to forward or backward on a small section. Where you do not turn anymore. For the traffic_sign, mofa, moped and motor_vehicle <strong>Can this be done with one checkbox?</strong> for forward or backward. And not with multiple checkboxes.</p>
<pre><code>&lt;item name=&quot;C12 &quot; icon=&quot;traffic_signs/NL/NL_C12.png&quot; type=&quot;node,way&quot;&gt;
        &lt;key key=&quot;traffic_sign&quot;value=&quot;NL:C12&quot; /&gt;
        &lt;key key=&quot;motor_vehicle&quot; value=&quot;no&quot; /&gt;
        &lt;key key=&quot;mofa&quot; value=&quot;yes&quot; /&gt;
        &lt;key key=&quot;moped&quot; value=&quot;yes&quot; /&gt;
&#10;        &lt;space /&gt;
        &lt;check key=&quot;traffic_sign:forward&quot; text=&quot;Forward motor_vehicle&quot; default=&quot;off&quot; value_off=&quot;&quot; value_on=&quot;NL:C12&quot; /&gt;
        &lt;check key=&quot;traffic_sign:backward&quot; text=&quot;Backward motor_vehicle&quot; default=&quot;off&quot; value_off=&quot;&quot; value_on=&quot;NL:C12&quot; /&gt;
        &lt;check key=&quot;motor_vehicle:forward&quot; text=&quot;Forward motor_vehicle&quot; default=&quot;off&quot; value_off=&quot;&quot; value_on=&quot;no&quot; /&gt;
        &lt;check key=&quot;motor_vehicle:backward&quot; text=&quot;Backward motor_vehicle&quot; default=&quot;off&quot; value_off=&quot;&quot; value_on=&quot;no&quot; /&gt;
        &lt;check key=&quot;mofa:forward&quot; text=&quot;Forward motor_vehicle&quot; default=&quot;off&quot; value_off=&quot;&quot; value_on=&quot;yes&quot; /&gt;
        &lt;check key=&quot;mofa:backward&quot; text=&quot;Backward motor_vehicle&quot; default=&quot;off&quot; value_off=&quot;&quot; value_on=&quot;yes&quot; /&gt;
        &lt;check key=&quot;moped:forward&quot; text=&quot;Forward motor_vehicle&quot; default=&quot;off&quot; value_off=&quot;&quot; value_on=&quot;yes&quot; /&gt;
        &lt;check key=&quot;moped:backward&quot; text=&quot;Backward motor_vehicle&quot; default=&quot;off&quot; value_off=&quot;&quot; value_on=&quot;yes&quot; /&gt;
&lt;/item&gt;</code></pre>
<p>Off course in above example the original k/v must be replaced by <em>:forward= or</em> :backward=</p>
<p>I can not find any solution in other presets.</p>
<p><strong>Is this possible?</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-forward" rel="tag" title="see questions tagged &#39;forward&#39;">forward</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-presets" rel="tag" title="see questions tagged &#39;presets&#39;">presets</span> <span class="post-tag tag-link-backward" rel="tag" title="see questions tagged &#39;backward&#39;">backward</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jul '17, 14:48</strong></p>
<img src="https://secure.gravatar.com/avatar/6c5dc0fc3be6786b643d15ec99ba3e3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Allroads&#39;s gravatar image" />
<p><span>Allroads</span><br />
<span class="score" title="222 reputation points">222</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Allroads has one accepted answer">10%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jul '17, 14:51</strong> </span></p>
</div>
</div>
<div id="comments-container-57286" class="comments-container">
&#10;</div>
<div id="comment-tools-57286" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57286-form-container" class="comment-form-container">
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

<span id="57357"></span>

<div id="answer-container-57357" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57357-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't believe this is possible directly, JOSM allows JAVA code in presets so probably there is a way to do it, but likely not easy.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '17, 20:49</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-57357" class="comments-container">
&#10;</div>
<div id="comment-tools-57357" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57357-form-container" class="comment-form-container">
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

