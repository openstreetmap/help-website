+++
type = "question"
title = "Create my own dissector"
description = '''Hi, i try to create a dissector for my own simple UDP-Command-Protocol.  -- Deklaration des neuen Protokolls   -- Proto(&quot;KurzName für FilterListbox&quot;, &quot;LangName&quot;)  UDP_CMD_proto = Proto(&quot;UDP-CMD&quot;,&quot;UDP-Command Protocol&quot;)   -- Deklaration der Felder im UDP_CMD_proto   local f = UDP_CMD_proto.fields  --...'''
date = "2011-06-06T09:43:00Z"
lastmod = "2011-06-07T23:45:00Z"
weight = 4410
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/4410" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Create my own dissector](/questions/4410/create-my-own-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4410-score" class="post-score" title="current number of votes">0</div><span id="post-4410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>i try to create a dissector for my own simple UDP-Command-Protocol.</p><pre><code>       -- Deklaration des neuen Protokolls 
       -- Proto(&quot;KurzName für FilterListbox&quot;, &quot;LangName&quot;) 
UDP_CMD_proto = Proto(&quot;UDP-CMD&quot;,&quot;UDP-Command Protocol&quot;)

       -- Deklaration der Felder im UDP_CMD_proto 
    local f = UDP_CMD_proto.fields
       -- .uint8(StatusText, &quot;Text&quot;, Hex-Ausgane, nil, welche Bits) 
      f.Flag1 = ProtoField.uint8(&quot;UDP_CMD_proto.Flag1&quot;, &quot;Response required&quot;, base.HEX, { [1] = &quot;YES&quot;, [0] = &quot;NO&quot;}, 0x01)
      f.Flag2 = ProtoField.uint8(&quot;UDP_CMD_proto.Flag2&quot;, &quot;...&quot;, base.HEX, nil, 0x02)
      f.Flag3 = ProtoField.uint8(&quot;UDP_CMD_proto.Flag3&quot;, &quot;...&quot;, base.HEX, nil, 0x04)
      f.Flag4 = ProtoField.uint8(&quot;UDP_CMD_proto.Flag4&quot;, &quot;...&quot;, base.HEX, nil, 0x08)
      f.Flag5 = ProtoField.uint8(&quot;UDP_CMD_proto.Flag5&quot;, &quot;...&quot;, base.HEX, nil, 0x10)
      f.Flag6 = ProtoField.uint8(&quot;UDP_CMD_proto.Flag6&quot;, &quot;...&quot;, base.HEX, nil, 0x20)
      f.Flag7 = ProtoField.uint8(&quot;UDP_CMD_proto.Flag7&quot;, &quot;...&quot;, base.HEX, nil, 0x40)
      f.Flag8 = ProtoField.uint8(&quot;UDP_CMD_proto.Flag8&quot;, &quot;...&quot;, base.HEX, nil, 0x80)

-------------------------------------------------------------
       -- Scriptfunktion zum &quot;sezieren&quot; der Protokolldaten
       -- mit Zugriff auf
       -- .dissector(PayloadData, InfoZeile, AnzeigeBaum)
function UDP_CMD_proto.dissector(buffer,pinfo,tree)

-------------
       -- Zugriff auf den Protokollnamen in der InfoZeile
    pinfo.cols.protocol = &quot;UDP-CMD&quot;
       -- Zugriff auf den InfoText in der InfoZeile
    if pinfo.dst_port == 33333 then
      pinfo.cols.info = &quot;Command         --&gt; PC&quot;
    end
    if pinfo.src_port == 33333 then
      pinfo.cols.info = &quot;PC-Response     --&gt; WIZ200&quot;
    end
    if pinfo.dst_port == 33334 then
      pinfo.cols.info = &quot;Command         --&gt; WIZ200&quot;
    end
    if pinfo.src_port == 33334 then
      pinfo.cols.info = &quot;WIZ200-Response --&gt; PC&quot;
    end
-------------

       -- Erstellung des AnzeigeBaumes für die PayloadData
       -- Neue main_TreeNode-Variable zum betehenden Tree (Frame, Ethernet, IP-Protokoll, UDP-Protokoll)
       -- tree:add(DISSECTOR, alleBytes, &quot;NameDerZeile&quot;) [wir brauchen nur einen Zeiger für den ganzen Baum!]          
    local TreeNode_E1 = tree:add(UDP_CMD_proto,buffer(),&quot;UDP-Command Protocol Data&quot;)

    TreeNode = TreeNode_E1:add(&quot;Source&quot;)    
      TreeNode:add(&quot;IP  :&quot;, pinfo.src)
      TreeNode:add(&quot;Port:&quot;, pinfo.src_port)

    TreeNode = TreeNode_E1:add(&quot;Destination&quot;)
      TreeNode:add(&quot;IP  :&quot;, pinfo.dst)
      TreeNode:add(&quot;Port:&quot;, pinfo.dst_port)

    local flags = buffer(0,1)
    TreeNode = TreeNode_E1:add(buffer(0,1), &quot;CommandFlags&quot;)
      TreeNode:add(f.Flag1, flags)
      TreeNode:add(f.Flag2, flags)
      TreeNode:add(f.Flag3, flags)
      TreeNode:add(f.Flag4, flags)
      TreeNode:add(f.Flag5, flags)
      TreeNode:add(f.Flag6, flags)
      TreeNode:add(f.Flag7, flags)
      TreeNode:add(f.Flag8, flags)

       -- Neuer Eintrag eine Ebene unterhalb der eben erstellten main_TreeNode-Variable        
       -- TreeNode:add(Byte(Pos, Count), Text .. Byte(Pos, Count)AsInteger  .. Text)

    TreeNode_E1:add(buffer(1,1),&quot;Modul Type:&quot; , buffer(1,1):uint())

    --TreeNode:add(buffer(1,1),&quot;Command    : &lt;&quot; .. buffer(1,1):uint() .. &quot;&gt;&quot;)
    --TreeNode:add(buffer(3),&quot;OptionalCMD: &quot; .. buffer(3):string())
-------------

end

       -- Zuweisung der UDP-Tabelle
udp_table = DissectorTable.get(&quot;udp.port&quot;)
       -- Zuweisung der zu überwachenden Ports
udp_table:add(33334,UDP_CMD_proto)
udp_table:add(33333,UDP_CMD_proto)</code></pre><p>With</p><pre><code>TreeNode = TreeNode_E1:add(&quot;Destination&quot;)
  TreeNode:add(&quot;IP  :&quot;, pinfo.src)
  TreeNode:add(&quot;Port:&quot;, pinfo.dst_port)</code></pre><p>I try to show the destination IP and Port, the Port filter works but the IP-filter don´t.</p><p>I also tryed : ip.src.....</p><p>How to show the soure and destination IP from the IP-Protocol part? Same Problem with the MAC-Address from the Ethernet part.</p><p>Thanks for your Help and excuse my bad english. Greets from the rainy Germany... Pfanne</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '11, 09:43</strong></p><img src="https://secure.gravatar.com/avatar/99abe74976c1c0ca886da31fed9feaa1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pfanne&#39;s gravatar image" /><p><span>Pfanne</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pfanne has no accepted answers">0%</span></p></div></div><div id="comments-container-4410" class="comments-container"></div><div id="comment-tools-4410" class="comment-tools"></div><div class="clear"></div><div id="comment-4410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="4411"></span>

<div id="answer-container-4411" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4411-score" class="post-score" title="current number of votes">2</div><span id="post-4411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>pinfo.src</code> returns an <a href="https://www.wireshark.org/docs/wsug_html_chunked/lua_module_Pinfo.html#lua_class_Address"><code>Address</code></a> <code>userdata</code> object (not <code>string</code>, which <code>tree:add()</code> requires). The same is true for:</p><ul><li><code>pinfo.dst</code></li><li><code>pinfo.dl_src</code></li><li><code>pinfo.dl_dst</code></li><li><code>pinfo.net_src</code></li><li><code>pinfo.net_dst</code></li></ul><p>You have to use <strong><code>tostring</code></strong> to get the string representation of the IP address. In your case:</p><pre><code>TreeNode = TreeNode_E1:add(&quot;Source&quot;)    
  TreeNode:add(&quot;IP  :&quot;, tostring(pinfo.src))
  TreeNode:add(&quot;Port:&quot;, pinfo.src_port)

TreeNode = TreeNode_E1:add(&quot;Destination&quot;)
  TreeNode:add(&quot;IP  :&quot;, tostring(pinfo.dst))
  TreeNode:add(&quot;Port:&quot;, pinfo.dst_port)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '11, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p><span>bstn</span><br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div></div><div id="comments-container-4411" class="comments-container"><span id="4412"></span><div id="comment-4412" class="comment"><div id="post-4412-score" class="comment-score"></div><div class="comment-text"><p>Jiiip, that´s the "missing link"</p><p>I try´d toString bevor but only in combination with - ip.src - UDP_CMD_proto.src</p><p>but never with pinfo.scr, the good was so near.. :-)</p><p>thanks....</p><p>Next Question: Is ist possible to add an If or an CASE query to this TreeNode</p><pre><code>TreeNode_E1:add(buffer(1,1),&quot;Modul Type:&quot; , buffer(1,1):uint())</code></pre><p>like this IF-statement</p><pre><code>f.Flag1 = ProtoField.uint8(&quot;UDP_CMD_proto.Flag1&quot;, &quot;Response required&quot;, base.HEX, { [1] = &quot;YES&quot;, [0] = &quot;NO&quot;}, 0x01)</code></pre><p>like this {[1]="Case1", [2]="Case2"}</p><p>thanks for your help..... :-) The lua-syntax is not may world.....</p></div><div id="comment-4412-info" class="comment-info"><span class="comment-age">(06 Jun '11, 12:00)</span> <span class="comment-user userinfo">Pfanne</span></div></div><span id="4414"></span><div id="comment-4414" class="comment"><div id="post-4414-score" class="comment-score"></div><div class="comment-text"><p>No, <code>TreeItem</code> can't lookup value-strings the way you describe, but it only takes an extra line of code to do what you need. In the following example, we use a <a href="http://lua-users.org/wiki/TablesTutorial">Lua table</a> to implement a value-string map:</p><pre><code>-- map &quot;yes&quot; and &quot;no&quot;
local VALS_YES_NO = {[1] = &quot;YES&quot;, [0] = &quot;NO&quot;}

-- add the 2nd byte as &quot;yes&quot; or &quot;no&quot; (default: &quot;no&quot;)
TreeNode_E1:add( buffer(1,1), &quot;Response required:&quot;, VALS_YES_NO[ buffer(1,1):uint() ] or &quot;NO&quot; )</code></pre></div><div id="comment-4414-info" class="comment-info"><span class="comment-age">(06 Jun '11, 12:58)</span> <span class="comment-user userinfo">bstn</span></div></div></div><div id="comment-tools-4411" class="comment-tools"></div><div class="clear"></div><div id="comment-4411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4444"></span>

<div id="answer-container-4444" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4444-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4444-score" class="post-score" title="current number of votes">1</div><span id="post-4444-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The following Lua gets you close (the format of the strings are slightly different):</p><pre><code>local idx0 = 6  -- start index
local idx1 = 11     -- end index

local asc = &quot;&quot;
local dec = &quot;&quot;
local hex = &quot;&quot;

-- Get the ASCII, decimal, and hex codes of each character
-- in the buffer between idx0 and idx1 and concatenate them
-- with a space delimiter
for i = idx0, idx1 do
    local c = buffer(i,1):uint()

    -- only append printable characters (hide garbage with spaces)
    if c &gt;= 0x20 and c &lt;= 0x7E then
        asc = string.format(&quot;%s %3c&quot;, asc, c)
    else
        asc = asc .. &quot;    &quot;
    end

    dec = string.format(&quot;%s %03d&quot;, dec, c)
    hex = string.format(&quot;%s %3x&quot;, hex, c)
end

TreeNode = TreeNode_E1:add(&quot;Value&quot;) 
TreeNode:add( buffer(idx0, idx1),   &quot;String     :&quot; , asc )
TreeNode:add( buffer(idx0, idx1),   &quot;Dezimal    :&quot; , dec )
TreeNode:add( buffer(idx0, idx1),   &quot;HEX        :&quot; , hex )</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '11, 14:26</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p><span>bstn</span><br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div></div><div id="comments-container-4444" class="comments-container"></div><div id="comment-tools-4444" class="comment-tools"></div><div class="clear"></div><div id="comment-4444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4441"></span>

<div id="answer-container-4441" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4441-score" class="post-score" title="current number of votes">0</div><span id="post-4441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>another great hint, thanks for it..... two more day and i will love the lua script language....</p><p>i think we have finished "our" little projekt soon.... :-) maybe the last problem:</p><p>i would like to constitute the last protokollbytes (Byte 6 to n) in all possible formats / vartypes e.g.:</p><pre><code>ASCII: H   a   l   l   o
DEC  : 072 097 108 108 111
HEX  : 48  61  6C  6C  6F</code></pre><p>How to add this to a treenode, absolutely we need to create a string in a for/next loop and add each formatet/transformed byte to the string. The main problem is..... right, the lua syntax for this....</p><pre><code>local VALS_Value = &quot;&quot;
for i = 6, 11, 1 do
  VALS_Value = VALS_Value + buffer(i):string()
end

TreeNode = TreeNode_E1:add(&quot;Value&quot;) 
  TreeNode:add(buffer(6),   &quot;String     :&quot; , buffer(6):string())
  TreeNode:add(buffer(6),   &quot;Dezimal    :&quot; , buffer(6):string())
  TreeNode:add(buffer(6),   &quot;HEX        :&quot; , buffer(6):string())
  TreeNode:add(VALS_Value)</code></pre><p>please can you help me again..... :-)</p><p>Thanks ands greeds from Hamburg Pfanne</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '11, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/99abe74976c1c0ca886da31fed9feaa1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pfanne&#39;s gravatar image" /><p><span>Pfanne</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pfanne has no accepted answers">0%</span></p></div></div><div id="comments-container-4441" class="comments-container"></div><div id="comment-tools-4441" class="comment-tools"></div><div class="clear"></div><div id="comment-4441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4450"></span>

<div id="answer-container-4450" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4450-score" class="post-score" title="current number of votes">0</div><span id="post-4450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi bstn,</p><p>thanks for your great help again.... :-) I will test this code soon as possible, when i´m at home.</p><pre><code>local idx1 = 11     -- end index</code></pre><p>the end index shoud be the last byte of the payload data....</p><pre><code>TreeNode:add( buffer(idx0),...</code></pre><p>could this be work: <code>local idx1 = pinfo.len</code> &lt;-- here we need the length of the payload data, i think this is the total lenght of the frame.</p><p>EDIT: What about --&gt; <code>buffer:len()</code> ??</p><p>Thanks Pfanne</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '11, 23:45</strong></p><img src="https://secure.gravatar.com/avatar/99abe74976c1c0ca886da31fed9feaa1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pfanne&#39;s gravatar image" /><p><span>Pfanne</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pfanne has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jun '11, 02:16</strong> </span></p></div></div><div id="comments-container-4450" class="comments-container"></div><div id="comment-tools-4450" class="comment-tools"></div><div class="clear"></div><div id="comment-4450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

