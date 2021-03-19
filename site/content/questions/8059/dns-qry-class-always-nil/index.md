+++
type = "question"
title = "dns qry class always nil?"
description = '''hello, I&#x27;m attempting to write a Lua tap to grab DNS info from some pcap files using tshark. I have one problem: every approach I&#x27;ve tried to get the dns.qry.class or dns.resp.class entities returns nil, even on packets that I know are dns packets (dns.qry.name, for example, isn&#x27;t nil). Example code...'''
date = "2011-12-20T11:27:00Z"
lastmod = "2011-12-24T03:23:00Z"
weight = 8059
keywords = [ "lua", "dns" ]
aliases = [ "/questions/8059" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [dns qry class always nil?](/questions/8059/dns-qry-class-always-nil)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8059-score" class="post-score" title="current number of votes">1</div><span id="post-8059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello,</p><p>I'm attempting to write a Lua tap to grab DNS info from some pcap files using tshark. I have one problem: every approach I've tried to get the dns.qry.class or dns.resp.class entities returns nil, even on packets that I know are dns packets (dns.qry.name, for example, isn't nil).</p><p>Example code:</p><pre><code>local class = Field.new(&#39;dns.qry.class&#39;)
function init_listener()
    local tap = Listener.new(&quot;ip&quot;)
    function tap.packet(pinfo,buffer, ip)
        if class() == nil then
           debug(&#39;class is nil&#39;)
        end
    end
end
init_listener()</code></pre><p>That bit of code always finds that the qry class is nil. I've tried downloading the nightly build of wireshark also, but that's giving me the same result. Does anyone have hints as to what I'm doing wrong here, or is there a bug in tshark's lua interface?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '11, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/1ec9bc298c29276d1ea9a047ddfb9746?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gclef&#39;s gravatar image" /><p><span>gclef</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gclef has no accepted answers">0%</span></p></div></div><div id="comments-container-8059" class="comments-container"></div><div id="comment-tools-8059" class="comment-tools"></div><div class="clear"></div><div id="comment-8059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8095"></span>

<div id="answer-container-8095" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8095-score" class="post-score" title="current number of votes">0</div><span id="post-8095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a bug either in the Lua interface or in the DNS dissector [which should probably be <a href="http://bugs.wireshark.org">reported</a>].</p><p>I recreated your symptom using the DNS <a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=view&amp;target=dns.cap">sample capture</a>. The interesting thing is that Wireshark knows which packets contain <code>dns.qry.class</code>, as indicated by the packet results after entering this field name into the Display Filter Textbox. So, one would think Lua would have the same benefit but apparently not.</p><p>For some reason, the same Lua tap can detect <code>dns.qry.class</code> in the mDNS <a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=view&amp;target=mDNS1.zip">sample capture</a>. To me, this suggests that the mDNS dissector might be doing something necessary for the Lua tap to work properly, and the DNS dissector isn't doing that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '11, 18:05</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-8095" class="comments-container"></div><div id="comment-tools-8095" class="comment-tools"></div><div class="clear"></div><div id="comment-8095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8101"></span>

<div id="answer-container-8101" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8101-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8101-score" class="post-score" title="current number of votes">0</div><span id="post-8101-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's a deficiency of the field specification in Lua. It uses the display filter string as identification of the field. But there's no guarantee of uniqueness of this string for each individual field.</p><p>If you look in the DNS dissector there are two fields using this filter string: hf_dns_qry_class and hf_dns_qry_class_mdns. The Lua script uses the latter, which isn't assigned a representation with your capture. It does get assigned one with the mDNS sample capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '11, 00:12</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-8101" class="comments-container"><span id="8111"></span><div id="comment-8111" class="comment"><div id="post-8111-score" class="comment-score"></div><div class="comment-text"><p>Thanks for this. I will probably file a bug, but, having not dug into the source code that much, I want to make sure I've got the bug wording right. Would this be clear enough: the lua field specification for dns fields should check both the hf_dns_qry_class and hf_dns_qry_class_mdns fields, and use whichever one has a value.</p><p>Thanks.</p></div><div id="comment-8111-info" class="comment-info"><span class="comment-age">(23 Dec '11, 08:22)</span> <span class="comment-user userinfo">gclef</span></div></div><span id="8117"></span><div id="comment-8117" class="comment"><div id="post-8117-score" class="comment-score"></div><div class="comment-text"><p>I would phrase the bug as "Lua should handle field names for which there are multiple registered fields"; this problem is <em>NOT</em> DNS-specific (X.25 also has multiple registered fields with the same name, for example, to handle both mod-8 and mod-128 mode).</p></div><div id="comment-8117-info" class="comment-info"><span class="comment-age">(23 Dec '11, 11:15)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="8127"></span><div id="comment-8127" class="comment"><div id="post-8127-score" class="comment-score"></div><div class="comment-text"><p>@gclef: Use your own wording referring to Lua, the DNS dissector is irrelevant in itself. Add a reference to this Ask item as an example.</p></div><div id="comment-8127-info" class="comment-info"><span class="comment-age">(24 Dec '11, 03:23)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-8101" class="comment-tools"></div><div class="clear"></div><div id="comment-8101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

