+++
type = "question"
title = "IPv6 Dissecting throws Lua FT not yet supported error! Why?"
description = '''I am using  field.IPV6 = ProtoField.ipv6 (&quot;IPv6&quot;, &quot;IPv6 Address&quot;)  subtree:add(IPv6, buffer(offset, 16) it throws LUA: FT not supported yet error. why do they then have in in the API reference? what&#x27;s going on?'''
date = "2013-08-02T09:19:00Z"
lastmod = "2014-03-07T16:21:00Z"
weight = 23519
keywords = [ "lua", "dissector", "error", "ipv6" ]
aliases = [ "/questions/23519" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [IPv6 Dissecting throws Lua FT not yet supported error! Why?](/questions/23519/ipv6-dissecting-throws-lua-ft-not-yet-supported-error-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23519-score" class="post-score" title="current number of votes">0</div><span id="post-23519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using field.IPV6 = ProtoField.ipv6 ("IPv6", "IPv6 Address")</p><p>subtree:add(IPv6, buffer(offset, 16)</p><p>it throws LUA: FT not supported yet error. why do they then have in in the API reference? what's going on?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '13, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/2ddc382640d092aeeba4db7267099715?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adityashankar&#39;s gravatar image" /><p><span>adityashankar</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adityashankar has no accepted answers">0%</span></p></div></div><div id="comments-container-23519" class="comments-container"></div><div id="comment-tools-23519" class="comment-tools"></div><div class="clear"></div><div id="comment-23519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="25104"></span>

<div id="answer-container-25104" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25104-score" class="post-score" title="current number of votes">1</div><span id="post-25104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From <a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/wslua/wslua_tree.c">wslua_tree.c</a></p><pre><code>static int TreeItem_add_item_any(lua_State *L, gboolean little_endian) {
...
            switch(type) {               
                case FT_IPv4:
                    item = proto_tree_add_ipv4(tree_item-&gt;tree,hfid,tvbr-&gt;tvb-&gt;ws_tvb,tvbr-&gt;offset,tvbr-&gt;len,*((guint32*)(checkAddress(L,1)-&gt;data)));
                    break;
                case FT_IPv6:
                case FT_IPXNET:
                case FT_GUID:
                case FT_OID:
                default:
                    luaL_error(L,&quot;FT_ not yet supported&quot;);
</code></pre><p>So, adding IPv6 items to the tree is not yet implemented, whereas it is for IPv4.</p><p><span><span>@adityashankar</span></span>: If you need that, please file an enhancement bug at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '13, 01:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-25104" class="comments-container"></div><div id="comment-tools-25104" class="comment-tools"></div><div class="clear"></div><div id="comment-25104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25167"></span>

<div id="answer-container-25167" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25167-score" class="post-score" title="current number of votes">1</div><span id="post-25167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think this is correct. I finally decided to write a quick Lua dissector to test this, and I was able to successfully add an IPv6 address.</p><p>Anyway, I deleted my original answer, and I'm too lazy to retype it, but I think it might have been the correct answer after all, or closer to it anyway.</p><p>In a nutshell though, try something along the lines of the following:</p><pre><code>local field_ipv6 = ProtoField.ipv6(&quot;foo.IPv6&quot;, &quot;IPv6 Address&quot;)

foo.fields = { ..., field_ipv6, ... }

subtree:add(field_ipv6, buffer(offset, 16)</code></pre><p>Refer to the <a href="http://www.wireshark.org/docs/wsug_html_chunked/wslua_dissector_example.html">User Guide</a> for more help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '13, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-25167" class="comments-container"><span id="25170"></span><div id="comment-25170" class="comment"><div id="post-25170-score" class="comment-score"></div><div class="comment-text"><p>let's make this your answer ;-)</p><p>I admit I did not check very thoroughly if that's the reason, although it looked reasonable to me. Do you mind to post the 'IPv6 dissector'? I would like to do some tests myself.</p><p>Regards<br />
Kurt</p></div><div id="comment-25170-info" class="comment-info"><span class="comment-age">(24 Sep '13, 13:06)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="25172"></span><div id="comment-25172" class="comment"><div id="post-25172-score" class="comment-score"></div><div class="comment-text"><p>Here is a <strong>VERY</strong> basic Lua dissector that you can start with. You will need to replace <code>FOO_PORT</code> with some port number of your choice and then run: <code>wireshark -X lua_script:foo.lua</code>.</p><pre><code>do
    -- Protocol
    local p_foo = Proto(&quot;foo&quot;, &quot;FOO Protocol&quot;)

    -- Fields
    local f_foo_val8 = ProtoField.uint8(&quot;foo.val8&quot;, &quot;Value 8&quot;, base.OCT)
    local f_foo_val16 = ProtoField.uint16(&quot;foo.val16&quot;, &quot;Value 16&quot;, base.DEC)
    local f_foo_val32 = ProtoField.uint32(&quot;foo.val32&quot;, &quot;Value 32&quot;, base.HEX)
    local f_foo_ipv4 = ProtoField.ipv4(&quot;foo.ipv4&quot;, &quot;IPv4 Address&quot;)
    local f_foo_ipv6 = ProtoField.ipv6(&quot;foo.ipv6&quot;, &quot;IPv6 Address&quot;)

    p_foo.fields = { f_foo_val8, f_foo_val16, f_foo_val32, f_foo_ipv4, f_foo_ipv6 }

    -- Dissection
    function p_foo.dissector(buf, pinfo, tree)
        local foo_tree = tree:add(p_foo, buf(0,-1))

        pinfo.cols.protocol:set(&quot;FOO&quot;)
        foo_tree:add(f_foo_val8, buf(0, 1))
        foo_tree:add(f_foo_val16, buf(1, 2))
        foo_tree:add(f_foo_val32, buf(3, 4))
        foo_tree:add(f_foo_ipv4, buf(7, 4))
        foo_tree:add(f_foo_ipv6, buf(11, 16))
    end

    -- Registration
    local udp_table = DissectorTable.get(&quot;udp.port&quot;)
    udp_table:add(FOO_PORT, p_foo)

end</code></pre></div><div id="comment-25172-info" class="comment-info"><span class="comment-age">(24 Sep '13, 13:21)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="25182"></span><div id="comment-25182" class="comment"><div id="post-25182-score" class="comment-score"></div><div class="comment-text"><p>I uploaded a sample capture file to cloudshark that this lua dissector will be able to dissect. See <a href="http://cloudshark.org/captures/965bd39c6694">http://cloudshark.org/captures/965bd39c6694</a> if you're interested. (If you decide to download it, you might want to download the original file, as there's a capture file comment in it that references this question to let you know how it was intended to be dissected.)</p><p>That aside, after thinking about this some more, I think we're missing some information, because the question clearly indicates, <em>it throws LUA: FT not supported yet error.</em>, so if that's the case, then it certainly does seem that Kurt's answer is the correct one.<br />
</p><p>However, I know for certain that <code>ProtoField.ipv6</code> works because I tested it. So, looking back at the question again (and after experimenting with Lua a bit), I now see:</p><pre><code>field.IPV6 = ProtoField.ipv6 (&quot;IPv6&quot;, &quot;IPv6 Address&quot;)
subtree:add(IPv6, buffer(offset, 16)</code></pre><p>Besides the poor naming convention of the filter (which isn't actually a problem in itself), there are a couple of syntax errors, the first of which is <code>field.IPV6</code>. This is an invalid name yielding an error dialog box that reads something along the lines of:</p><pre><code>Lua: syntax error during precompilation of &#39;foo.lua&#39;:
[string &quot;foo.lua&quot;]:11: unexpected symbol near &#39;.&#39; [OK]</code></pre><p>So let's assume <code>field_IPV6</code> was intended, but then the next line should be:</p><pre><code>subtree:add(field_IPV6, buffer(offset, 16)</code></pre><p>So I tested this too, passing the invalid original <code>IPv6</code> instead of <code>field_IPV6</code>, but Wireshark seems to start up just fine without any indications of any errors. The field doesn't get added to the tree of course, but there's no error message either. So basically I can't reproduce what <span></span><span>@adityashankar</span> reported given only the information provided. Maybe someone else can or maybe <span></span><span>@adityashankar</span> can provide some additional information.</p></div><div id="comment-25182-info" class="comment-info"><span class="comment-age">(24 Sep '13, 18:07)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="25203"></span><div id="comment-25203" class="comment"><div id="post-25203-score" class="comment-score"></div><div class="comment-text"><p>thanks for the code and the capture file. I'll have a look.</p><blockquote><p>maybe <span>@adityashankar</span> can provide some additional information.</p></blockquote><p>I think we need the original code that caused the error message to understand what's going on.</p></div><div id="comment-25203-info" class="comment-info"><span class="comment-age">(25 Sep '13, 04:11)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-25167" class="comment-tools"></div><div class="clear"></div><div id="comment-25167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30587"></span>

<div id="answer-container-30587" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30587-score" class="post-score" title="current number of votes">1</div><span id="post-30587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This question is old, but since I know the answer I figured I'd answer it in case someone finds this Q&amp;A topic through the much-maligned ask.wireshark.org search algorithm (or just via google):</p><p>The reason the original ask'er would get that error, but not in cmaynard's script, is because the treeitem:add() method does different things depending on the number of arguments and argument types it gets. (in other words it has multiple function prototypes/signatures) In fact one might say it has <em>too many</em> possible signatures, because it's really confusing.</p><p>When it's called with a first argument of a Proto or ProtoField, and a second argument of a TvbRange, and no more arguments than that, then it adds the given field type to the tree based on the given tvbrange. In that case, using an IPv6-based field is fine.</p><p>That's what happens in cmaynard's script when it does this:</p><pre><code>foo_tree:add(f_foo_ipv6, buf(11, 16))</code></pre><p>Since that has only two arguments, and the first one is a ProtoField and the second is a TvbRange, it'll add the TVB's bytes starting at offset 11 for length 16, as an IPv6 address into the tree.</p><p>But if there were a <em>third</em> argument to treeitem:add(), then the third argument is a <strong>value</strong>, to be used for the field in the tree display. The TvbRange (second argument) would still be used, to highlight in the bytes window pane where the value is, but the value third argument is used for the value shown in the details pane and filters and such. Unfortunately, in that model, one cannot use an IPv6 field type for the first argument. (probably because it would be a pain to handle a value being passed in from Lua for that, since an IPv6 value can't be represented by a number or boolean)</p><p>The reason I say the function is too confusing, however, is because it also has other signatures: if the first argument is a Proto or ProtoField and the second argument is <strong>not</strong> a TvbRange, but is instead something else, then that <em>second</em> argument is treated as the <strong>value</strong> to be set, and again if the first argument is a IPv6 field type, then again you can't do it and will hit this error.</p><p>But wait, don't act yet! We'll also throw in a free steak knife set... because the treeitem:add() has other signatures too, including ones where there are neither Proto/ProtoField nor TvbRange, and one where the first argument is a TvbRange and the second is a string, and another where there's only a TvbRange argument.</p><p>So I guess one could say the function is very flexible and accommodating. :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '14, 16:21</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span> </br></br></p></div></div><div id="comments-container-30587" class="comments-container"></div><div id="comment-tools-30587" class="comment-tools"></div><div class="clear"></div><div id="comment-30587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

