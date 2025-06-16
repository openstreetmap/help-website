+++
type = "question"
title = "Own Nominatim Server gives no JSON output in Curl"
description = '''Hello, my own nomination server works well. In Chrome I get my JSON output: [  {  &quot;place_id&quot;: &quot;6781110&quot;,  &quot;licence&quot;: &quot;Data © OpenStreetMap contributors, ODbL 1.0. https://www.openstreetmap.org/copyright&quot;,  &quot;osm_type&quot;: &quot;way&quot;,  &quot;osm_id&quot;: &quot;35776867&quot;,  &quot;boundingbox&quot;: [  &quot;52.5531628&quot;,  &quot;52.5534904&quot;,  &quot;13....'''
date = "2016-11-19T22:24:00Z"
lastmod = "2016-11-20T08:53:00Z"
weight = 53042
keywords = [ "curl", "nominatim" ]
aliases = [ "/questions/53042" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Own Nominatim Server gives no JSON output in Curl](/questions/53042/own-nominatim-server-gives-no-json-output-in-curl)

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
<span id="post-53042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53042-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>my own nomination server works well. In Chrome I get my JSON output:</p>
<pre><code>[
    {
        &quot;place_id&quot;: &quot;6781110&quot;,
        &quot;licence&quot;: &quot;Data © OpenStreetMap contributors, ODbL 1.0. https://www.openstreetmap.org/copyright&quot;,
        &quot;osm_type&quot;: &quot;way&quot;,
        &quot;osm_id&quot;: &quot;35776867&quot;,
        &quot;boundingbox&quot;: [
            &quot;52.5531628&quot;,
            &quot;52.5534904&quot;,
            &quot;13.3737733&quot;,
            &quot;13.3743485&quot;
        ],
        &quot;lat&quot;: &quot;52.55333255&quot;,
        &quot;lon&quot;: &quot;13.3739065743598&quot;,
        &quot;display_name&quot;: &quot;20, Gottschedstraße, Gesundbrunnen, Mitte, Berlin, 13357, Deutschland&quot;,
        &quot;class&quot;: &quot;building&quot;,
        &quot;type&quot;: &quot;yes&quot;,
        &quot;importance&quot;: 0.101
    }
]</code></pre>
<p>but in my linux bash I get with: curl -H "Content-type: text/html; charset=UTF-8" http://sgwtest.ddns.net/nominatim/search.php?q=13357+gottschedstraße+20&amp;format=json</p>
<p>I get only the HTML-part like:</p>
<pre><code>&lt;!DOCTYPE html&gt; &lt;html lang=&quot;en&quot;&gt; &lt;head&gt;
    &lt;title&gt;OpenStreetMap Nominatim: Search&lt;/title&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&#10;    &lt;base href=&quot;/nominatim/&quot; /&gt;
    &lt;link href=&quot;nominatim.xml&quot; rel=&quot;search&quot; title=&quot;Nominatim Search&quot; type=&quot;application/opensearchdescription+xml&quot; /&gt;
    &lt;link href=&quot;css/leaflet.css&quot; rel=&quot;stylesheet&quot; /&gt;
    &lt;link href=&quot;css/bootstrap-theme.min.css&quot; rel=&quot;stylesheet&quot; /&gt;
    &lt;link href=&quot;css/bootstrap.min.css&quot; rel=&quot;stylesheet&quot; /&gt;
    &lt;link href=&quot;css/common.css&quot; rel=&quot;stylesheet&quot; type=&quot;text/css&quot; /&gt;
    &lt;link href=&quot;css/search.css&quot; rel=&quot;stylesheet&quot; type=&quot;text/css&quot; /&gt; &lt;/head&gt;</code></pre>
<p>But why? In chrome it works very well, why not with curl</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-curl" rel="tag" title="see questions tagged &#39;curl&#39;">curl</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '16, 22:24</strong></p>
<img src="https://secure.gravatar.com/avatar/ad332fb85ece95d8d53ae63eea5d534f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hevilp&#39;s gravatar image" />
<p><span>hevilp</span><br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hevilp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53042" class="comments-container">
&#10;</div>
<div id="comment-tools-53042" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53042-form-container" class="comment-form-container">
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

<span id="53044"></span>

<div id="answer-container-53044" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53044-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-53044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hevilp has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have really entered the <code>curl</code> command as written, then your shell has cut off everything after the first <code>&amp;</code> which on Unix is traditionally a way to end a command and send it to the background. You have to add quotes around the URL, like so:</p>
<pre><code>curl &quot;http://sgwtest.ddns.net/nominatim/search.php?q=13357+gottschedstraße+20&amp;format=json&quot;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '16, 23:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-53044" class="comments-container">
<span id="53048"></span>
<div id="comment-53048" class="comment">
<div id="post-53048-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>this helped, thank you!</p>
</div>
<div id="comment-53048-info" class="comment-info">
<span class="comment-age">(20 Nov '16, 08:53)</span> <span class="comment-user userinfo">hevilp</span>
</div>
</div>
</div>
<div id="comment-tools-53044" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53044-form-container" class="comment-form-container">
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

