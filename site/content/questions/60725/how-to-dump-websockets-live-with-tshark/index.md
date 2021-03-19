+++
type = "question"
title = "How to dump websockets live with tshark?"
description = '''Websocket text is masked and isn&#x27;t viewable with tcpdump. Trying to see it with this: tshark -e websocket.payload.text_unmask -Tfields port 1234  There was a websocket.payload.text_unmask filter, but where it&#x27;s gone in 2.0.2?'''
date = "2017-04-11T00:05:00Z"
lastmod = "2017-05-09T06:43:00Z"
weight = 60725
keywords = [ "mask", "websocket", "tshark" ]
aliases = [ "/questions/60725" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to dump websockets live with tshark?](/questions/60725/how-to-dump-websockets-live-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60725-score" class="post-score" title="current number of votes">0</div><span id="post-60725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Websocket text is masked and isn't viewable with tcpdump. Trying to see it with this:</p><pre><code>tshark -e websocket.payload.text_unmask -Tfields port 1234</code></pre><p>There was a <code>websocket.payload.text_unmask</code> filter, but where it's gone in 2.0.2?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mask" rel="tag" title="see questions tagged &#39;mask&#39;">mask</span> <span class="post-tag tag-link-websocket" rel="tag" title="see questions tagged &#39;websocket&#39;">websocket</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '17, 00:05</strong></p><img src="https://secure.gravatar.com/avatar/61aed86d6beb415fed90e3f2ecbb0cbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chip-devel&#39;s gravatar image" /><p><span>chip-devel</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chip-devel has no accepted answers">0%</span></p></div></div><div id="comments-container-60725" class="comments-container"></div><div id="comment-tools-60725" class="comment-tools"></div><div class="clear"></div><div id="comment-60725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="60789"></span>

<div id="answer-container-60789" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60789-score" class="post-score" title="current number of votes">1</div><span id="post-60789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <code>websocket.payload.text_unmask</code> field was removed in Wireshark 2.0, this filter would not always exist (namely, when payloads were not masked). The <code>websocket.payload</code> field is supposed to be the replacement, but it appears that its field type unfortunately does not allow operators like <code>websocket.payload contains "Rock"</code> (it is a <code>FT_NONE</code> rather than a <code>FT_BYTES</code> field type).</p><p>Note that the <code>websocket.payload</code> field also contains the data for <a href="https://tools.ietf.org/html/rfc6455#section-5.5">control frames</a> so it is likely not what you want.</p><p>Depending on the Websocket preference "Dissect websocket text as", you can control that the data is displayed as Line-based text (the default), JSON or SIP. For your type of data (lines of text) it is unfortunately not possible to add a filter to extract this data.</p><p>If you would like to do so, you could write a subdissector for Websockets data. This will take precedence over the fallback to Line-based text. Example Lua dissector:</p><pre><code>local myproto = Proto(&quot;myproto&quot;, &quot;Websocket Text&quot;)
myproto.fields.text = ProtoField.string(&quot;myproto.text&quot;, &quot;Websocket text&quot;)
function myproto.dissector(tvb, pinfo, tree)
    tree:add(myproto.fields.text, tvb())
end
local function myproto_heur(tvb, pinfo, tree)
    myproto.dissector(tvb, pinfo, tree)
    return true -- accept all Websockets data (do not call other dissectors)
end
myproto:register_heuristic(&quot;ws&quot;, myproto_heur)</code></pre><p>Example usage:</p><pre><code>tshark -r out.pcap -Xlua_script:ws.lua -Tfields -e myproto.text</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '17, 14:44</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Apr '17, 14:44</strong> </span></p></div></div><div id="comments-container-60789" class="comments-container"><span id="61308"></span><div id="comment-61308" class="comment"><div id="post-61308-score" class="comment-score"></div><div class="comment-text"><p>Doesn't read what iocat tool produces.</p></div><div id="comment-61308-info" class="comment-info"><span class="comment-age">(09 May '17, 06:43)</span> <span class="comment-user userinfo">chip-devel</span></div></div></div><div id="comment-tools-60789" class="comment-tools"></div><div class="clear"></div><div id="comment-60789-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60729"></span>

<div id="answer-container-60729" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60729-score" class="post-score" title="current number of votes">0</div><span id="post-60729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try the field "websocket.payload".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '17, 02:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60729" class="comments-container"><span id="60737"></span><div id="comment-60737" class="comment"><div id="post-60737-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately it prints mostly empty lines.</p></div><div id="comment-60737-info" class="comment-info"><span class="comment-age">(11 Apr '17, 05:36)</span> <span class="comment-user userinfo">chip-devel</span></div></div><span id="60738"></span><div id="comment-60738" class="comment"><div id="post-60738-score" class="comment-score"></div><div class="comment-text"><p>We'll need to see a capture to help any further.</p><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, Dropbox?</p></div><div id="comment-60738-info" class="comment-info"><span class="comment-age">(11 Apr '17, 06:09)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="60739"></span><div id="comment-60739" class="comment"><div id="post-60739-score" class="comment-score"></div><div class="comment-text"><p>Rolled back to the 1.10.6 - 'websocket.payload.text_unmask' works. Testing now with <a href="http://www.websocket.org/echo.html">http://www.websocket.org/echo.html</a> - Wireshark shows the contents, but tshark doesn't, capture: <a href="https://drive.google.com/open?id=0B-8YrNWvmVCgX2hVbDBaWkgzZTQ">https://drive.google.com/open?id=0B-8YrNWvmVCgX2hVbDBaWkgzZTQ</a></p></div><div id="comment-60739-info" class="comment-info"><span class="comment-age">(11 Apr '17, 08:05)</span> <span class="comment-user userinfo">chip-devel</span></div></div><span id="60741"></span><div id="comment-60741" class="comment"><div id="post-60741-score" class="comment-score"></div><div class="comment-text"><p>Try this:</p><pre><code>tshark -r out.pcap -Y websocket.payload -E occurrence=l -T fields -e text</code></pre><p>The unmasked text is handed off to the "Line-Based text data" dissector, so you need to use the field selector for that, and also set the occurrence to the last instance of that field in the packet to remove "noise". I've also added a filter to limit the output to packets that contain a websocket payload.</p></div><div id="comment-60741-info" class="comment-info"><span class="comment-age">(11 Apr '17, 08:42)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-60729" class="comment-tools"></div><div class="clear"></div><div id="comment-60729-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

