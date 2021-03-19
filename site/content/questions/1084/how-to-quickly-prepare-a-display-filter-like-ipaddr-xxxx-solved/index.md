+++
type = "question"
title = "How to quickly prepare a Display filter like &quot;ip.addr == x.x.x.x&quot; ? (solved)"
description = '''While displaying an interesting packet, it is often needed to filter all traffic on an IP address, but not only as source or destination as the right-click filtering permits in the main GUI window. Actually, I prepare a filter like ip.src == x.x.x.x then replace src by addr to get what all traffic t...'''
date = "2010-11-23T10:42:00Z"
lastmod = "2011-12-04T11:38:00Z"
weight = 1084
keywords = [ "filter", "lua" ]
aliases = [ "/questions/1084" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [How to quickly prepare a Display filter like "ip.addr == x.x.x.x" ? (solved)](/questions/1084/how-to-quickly-prepare-a-display-filter-like-ipaddr-xxxx-solved)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1084-score" class="post-score" title="current number of votes">1</div><span id="post-1084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>While displaying an interesting packet, it is often needed to filter all traffic on an IP address, but not only as source or destination as the right-click filtering permits in the main GUI window.</p><p>Actually, I prepare a filter like <code>ip.src == x.x.x.x</code> then replace <code>src</code> by <code>addr</code> to get what all traffic to/from this host.</p><p>Is there another way to create it from the main GUI window?</p><p>[edit]: a Lua script permits to quickly build the filter, see below</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '10, 10:42</strong></p><img src="https://secure.gravatar.com/avatar/449c0829813aecd7a23d1f4992e1e5b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="S%20Peters&#39;s gravatar image" /><p><span>S Peters</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="S Peters has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Nov '11, 14:16</strong> </span></p></div></div><div id="comments-container-1084" class="comments-container"><span id="7655"></span><div id="comment-7655" class="comment"><div id="post-7655-score" class="comment-score"></div><div class="comment-text"><p>I'm glad to see that this field has been included in the main GUI window! At least since version 1.6.3, which permits to select eg ip.src, ip.addr, ip.src_host or ip.host with one click, so that this question has found its answer.</p></div><div id="comment-7655-info" class="comment-info"><span class="comment-age">(26 Nov '11, 14:16)</span> <span class="comment-user userinfo">S Peters</span></div></div></div><div id="comment-tools-1084" class="comment-tools"></div><div class="clear"></div><div id="comment-1084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

5 Answers:

</div>

</div>

<span id="1159"></span>

<div id="answer-container-1159" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1159-score" class="post-score" title="current number of votes">2</div><span id="post-1159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>At last, I have written a Lua post-dissector that match my needs, adapted from the "trivial" pseudo-protocol seen in the Lua tutorial; it adds an "Endpoints" element to the tree, that permits to "Prepare" an ip.addr filter :</p><pre><code>-- ip-addr postdissector example
-- declare some Fields to be read
ip_src_f = Field.new(&quot;ip.src&quot;)
ip_dst_f = Field.new(&quot;ip.dst&quot;)

-- declare our (pseudo) protocol
endpoints_proto = Proto(&quot;endpoints&quot;,&quot;Endpoints list&quot;)
-- create the fields for our &quot;protocol&quot;
src_F = ProtoField.string(&quot;ip.addr&quot;,&quot;Source&quot;)
dst_F = ProtoField.string(&quot;ip.addr&quot;,&quot;Destination&quot;)
-- add the field to the protocol
endpoints_proto.fields = {src_F, dst_F}
-- create a function to &quot;postdissect&quot; each frame
function endpoints_proto.dissector(buffer,pinfo,tree)
    -- obtain the current values the protocol fields
    local ip_src = ip_src_f()
    local ip_dst = ip_dst_f()
    if ip_src then
       local subtree = tree:add(endpoints_proto,&quot;IP Endpoints&quot;)
       local src = tostring(ip_src) 
       local dst = tostring(ip_dst)
       subtree:add(src_F,src)
       subtree:add(dst_F,dst)

    end
end
-- register our protocol as a postdissector
register_postdissector(endpoints_proto)</code></pre><p>Here is the resulting tree element, seen in the middle pane:</p><pre><code>-----------------------
[-] Endpoints
    Source: 10.0.0.1
    Destination: 10.0.0.2
-----------------------</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '10, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/449c0829813aecd7a23d1f4992e1e5b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="S%20Peters&#39;s gravatar image" /><p><span>S Peters</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="S Peters has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Nov '10, 04:46</strong> </span></p></div></div><div id="comments-container-1159" class="comments-container"></div><div id="comment-tools-1159" class="comment-tools"></div><div class="clear"></div><div id="comment-1159-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7762"></span>

<div id="answer-container-7762" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7762-score" class="post-score" title="current number of votes">2</div><span id="post-7762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>They are just hidden; to make the pseudo-fields (<code>ip.addr</code>, <code>ip.host</code> etc.) appear, choose :</p><pre><code>Edit - Preferences - Protocols - Display hidden protocols items</code></pre><p>Then the field giving the <code>ip.addr</code> filter is found in the middle pane, and looks like this:</p><pre><code>&lt;Source or Destination Address : 10.1.2.3(10.1.2.3)&gt;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '11, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/449c0829813aecd7a23d1f4992e1e5b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="S%20Peters&#39;s gravatar image" /><p><span>S Peters</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="S Peters has no accepted answers">0%</span></p></div></div><div id="comments-container-7762" class="comments-container"></div><div id="comment-tools-7762" class="comment-tools"></div><div class="clear"></div><div id="comment-7762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1085"></span>

<div id="answer-container-1085" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1085-score" class="post-score" title="current number of votes">1</div><span id="post-1085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, this is not possible from the GUI for the IP addresses. For ethernet addresses, it is possible, if you open the packet details and expnd the source or destination mac-address, the address will be listed again, this time without source or destination. You can now use "Apply as filter" and it will use eth.addr instead of eth.src or eth.dst.</p><p>If you would find it useful to have this for IP addresses too, you might want to open up an enhancement request on <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '10, 11:16</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1085" class="comments-container"><span id="1101"></span><div id="comment-1101" class="comment"><div id="post-1101-score" class="comment-score"></div><div class="comment-text"><p>And consider whether you'd want such a filter to EXCLUDE that traffic as well...</p></div><div id="comment-1101-info" class="comment-info"><span class="comment-age">(23 Nov '10, 18:54)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div></div><div id="comment-tools-1085" class="comment-tools"></div><div class="clear"></div><div id="comment-1085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1104"></span>

<div id="answer-container-1104" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1104-score" class="post-score" title="current number of votes">1</div><span id="post-1104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, like Sake said, there isn't an "ip.addr" field in the packet to right-click on.</p><p>Given that I'm a lousy tpyist, I'd probably rather pull the ip.addr== from a pre-made filter. The image below shows one of my display filter sets... (the IP address filter doesn't have the exclamation point at the beginning in the string). I'd rather click than type any day &lt;g&gt;. Oh sure, Wireshark complains a bit as the filter isn't completed, but I don't have to backspace or type in the beginning, so it works for me.</p><p>BTW, I edited the order in Notepad (and added the separator and indents)...</p><p><img src="http://www.wiresharktraining.com/ask/dfilter1.jpg" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '10, 19:31</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></img></div></div><div id="comments-container-1104" class="comments-container"></div><div id="comment-tools-1104" class="comment-tools"></div><div class="clear"></div><div id="comment-1104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1123"></span>

<div id="answer-container-1123" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1123-score" class="post-score" title="current number of votes">0</div><span id="post-1123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Too bad for the Gui, and the usage of filters isn't so easy as I hoped.</p><p>Perhaps with some Lua scripts ?</p><p>This one is really too simple, but seems to go in the right direction, without requiring too much clicks.</p><pre><code>-- put this script in your init.lua file, and click on the Tools menu 
-- to copy the desired string in the clipboard
function stringipaddr()       copy_to_clipboard(&quot;ip.addr == &quot;) end
function stringnotipaddr()    copy_to_clipboard(&quot;!ip.addr == &quot;) end

register_menu(&quot;Copy string \&quot;ip.addr == \&quot;&quot;, stringipaddr,   MENU_TOOLS_UNSORTED)
register_menu(&quot;Copy string \&quot;!ip.addr == \&quot;&quot;,stringnotipaddr,MENU_TOOLS_UNSORTED)</code></pre><p>If I understand the concepts of Lua well, it could even be possible to register a new element to the right-click menu. I hope to find something about it soon, otherwise the enhancement request on the list will be the choice.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '10, 10:59</strong></p><img src="https://secure.gravatar.com/avatar/449c0829813aecd7a23d1f4992e1e5b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="S%20Peters&#39;s gravatar image" /><p><span>S Peters</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="S Peters has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Nov '10, 10:59</strong> </span></p></div></div><div id="comments-container-1123" class="comments-container"></div><div id="comment-tools-1123" class="comment-tools"></div><div class="clear"></div><div id="comment-1123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

