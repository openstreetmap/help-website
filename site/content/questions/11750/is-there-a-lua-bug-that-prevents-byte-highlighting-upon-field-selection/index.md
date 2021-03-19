+++
type = "question"
title = "Is there a Lua bug that prevents byte highlighting upon field selection?"
description = '''The following Lua does not highlight the corresponding bytes upon field selection (for f_length): version = &quot;0.1&quot;; workPort = 3003;  full_name = &quot;Service Control Point protocol&quot;; short_name = &quot;SCP&quot;; perent_port = &quot;tcp.port&quot;; SCP_proto = Proto(short_name,full_name); local f_length = ProtoField.uint32...'''
date = "2012-06-08T01:54:00Z"
lastmod = "2012-06-08T03:23:00Z"
weight = 11750
keywords = [ "lua" ]
aliases = [ "/questions/11750" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a Lua bug that prevents byte highlighting upon field selection?](/questions/11750/is-there-a-lua-bug-that-prevents-byte-highlighting-upon-field-selection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11750-score" class="post-score" title="current number of votes">1</div><span id="post-11750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The following Lua does not highlight the corresponding bytes upon field selection (for <code>f_length</code>):</p><pre><code>version = &quot;0.1&quot;;
workPort = 3003; 
full_name = &quot;Service Control Point protocol&quot;;
short_name = &quot;SCP&quot;;
perent_port = &quot;tcp.port&quot;;
SCP_proto = Proto(short_name,full_name);
local f_length = ProtoField.uint32(&quot;length&quot;, &quot;length&quot;);
SCP_proto.fields = {
    f_length
    }
function SCP_proto.dissector (buf, pkt, root)
    pkt.cols.protocol = SCP_proto.name
    subtree = root:add(SCP_proto, buf(0));
    subtree:append_text(&quot;(using BER),version &quot;..version..&quot; by SMT-ICC&quot;);

    local length = subtree:add(f_length,buf(0,4):le_uint() );
end

function SCP_proto.init()
end

local tcp_dissector_table = DissectorTable.get(perent_port)
dissector = tcp_dissector_table:get_dissector(workPort)
tcp_dissector_table:add(workPort, SCP_proto)</code></pre><p>...but this <em>does</em>:</p><pre><code>function SCP_proto.dissector (buf, pkt, root)
    ...
    local length = subtree:add(f_length,buf(0,4));
    local length_v = buf(0,4):le_uint();
    length:set_text(&quot;length:\t&quot; .. length_v)
end</code></pre><p>Is this a Wireshark 1.7.x bug or a problem with my code above?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '12, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/3763e1738205d07231e2d6fc4ff01a35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PavelMSTU&#39;s gravatar image" /><p><span>PavelMSTU</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PavelMSTU has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jun '12, 03:20</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11750" class="comments-container"></div><div id="comment-tools-11750" class="comment-tools"></div><div class="clear"></div><div id="comment-11750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11751"></span>

<div id="answer-container-11751" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11751-score" class="post-score" title="current number of votes">4</div><span id="post-11751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="PavelMSTU has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is not a Wireshark bug. You just happen to be exercising one of the features of <code>TreeItem.add()</code>.</p><p><a href="http://wiki.wireshark.org/LuaAPI/TreeItem#treeitem:add.28proto_field_.5B.2Ctvbrange.5D_.5B.2Cvalue_.5B.2Ctext1_.5B.2Ctext2.5D_....5D_.5D.29"><code>TreeItem.add()</code></a> takes a <code>ProtoField</code> and a <code>TvbRange</code> as parameters. The <code>ProtoField</code> specifies the field's label and the format of the raw data (among other things). The <code>TvbRange</code> contains the raw data to be parsed. Given the <code>ProtoField</code> and the <code>TvbRange</code>, the <code>TreeItem</code> knows how to parse the raw data, adding the labeled value to the protocol tree and highlighting the bytes that correspond to the <code>TvbRange</code> upon field selection.</p><p>However, the <code>TvbRange</code> parameter in <code>TreeItem.add()</code> is <strong>optional</strong>. The <code>TreeItem</code> will happily take a literal value instead, which allows one to add tree items without a backing buffer (e.g., generated analysis items based on earlier traffic). And this is what you are unintentionally doing with this line of code:</p><pre><code>local length = subtree:add(f_length,buf(0,4):le_uint());</code></pre><p>Here's a quick breakdown of the two arguments:</p><ul><li><code>f_length</code> is a <strong><code>ProtoField</code></strong></li><li><code>buf(0,4):le_uint()</code> returns a Lua <strong><code>number</code></strong>, which is a literal value</li></ul><p>Since the arguments passed to <code>TreeItem.add()</code> do not include a <code>TvbRange</code>, <code>TreeItem</code> does not know what to highlight. It simply adds the labeled value to the protocol tree.</p><p>In your rewritten code, you saw that this line:</p><pre><code>local length = subtree:add(f_length,buf(0,4));</code></pre><p>achieved your intermediate goal of highlighting the field's bytes upon field selection. This is because you're now passing the <code>TvbRange</code> needed by <code>TreeItem</code>.</p><p><strong>But</strong> then you must've realized that the field value was wrong because it was shown in big-endian when you needed little-endian, so you compensated by parsing the little-endian integer from the <code>TvbRange</code> and setting the <code>TreeItem</code>'s text accordingly:</p><pre><code>local length_v = buf(0,4):le_uint();
length:set_text(&quot;length:\t&quot; .. length_v)</code></pre><p>Actually, this is unnecessary (and inefficient). These three lines in your rewritten code can be simplified into one by using <a href="http://wiki.wireshark.org/LuaAPI/TreeItem#treeitem:add_le.28proto_field_.5B.2Ctvbrange.5D_.5B.2Cvalue_.5B.2Ctext1_.5B.2Ctext2.5D_....5D_.5D.29"><code>TreeItem.add_le()</code></a>:</p><pre><code>subtree:add_le(f_length,buf(0,4));</code></pre><p>Note that <code>TreeItem.add()</code> uses big-endian format, and you should be able to guess what <code>TreeItem.add_le()</code> does. :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '12, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-11751" class="comments-container"><span id="11752"></span><div id="comment-11752" class="comment"><div id="post-11752-score" class="comment-score"></div><div class="comment-text"><p>thanks you!</p></div><div id="comment-11752-info" class="comment-info"><span class="comment-age">(08 Jun '12, 03:23)</span> <span class="comment-user userinfo">PavelMSTU</span></div></div></div><div id="comment-tools-11751" class="comment-tools"></div><div class="clear"></div><div id="comment-11751-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

