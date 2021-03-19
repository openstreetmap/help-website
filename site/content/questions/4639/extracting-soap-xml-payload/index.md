+++
type = "question"
title = "Extracting SOAP XML Payload"
description = '''Using Lua and Tshark I&#x27;m attempting to obtain the XML payload from SOAP messages exchanged with my web service. I went with a listener approach (see program below), but it doesn&#x27;t appear to be working properly. The s_xml_cdata print statement simply prints &quot;RB14&quot;. I don&#x27;t receive the full XML. Admit...'''
date = "2011-06-20T11:51:00Z"
lastmod = "2011-06-30T11:04:00Z"
weight = 4639
keywords = [ "xml", "lua", "extract", "tshark", "soap" ]
aliases = [ "/questions/4639" ]
osqa_answers = 12
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting SOAP XML Payload](/questions/4639/extracting-soap-xml-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4639-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using Lua and Tshark I'm attempting to obtain the XML payload from SOAP messages exchanged with my web service. I went with a listener approach (see program below), but it doesn't appear to be working properly. The s_xml_cdata print statement simply prints "RB14". I don't receive the full XML. Admittedly I'm new to both Tshark and Lua so I may be making some rookie mistakes here. I scoured the Web for any examples, but I've yet to come up with anything helpful. My ultimate goal is to save the SOAP XML to a flat file and/or redirect to a named pipe.</p><pre><code>xml_cdata_f = Field.new(&quot;xml.cdata&quot;)
xml_tag_f = Field.new(&quot;xml.tag&quot;)

local tap = Listener.new(nil, &quot;xml&quot; )

function tap.packet(pinfo, pvb, xml)

  print(&quot;\nTap Hit!&quot;)

  local s_xml_cdata = tostring(xml_cdata_f())  
  local s_xml_tag = tostring(xml_tag_f())

  print(&quot;\n&quot; .. s_xml_cdata)  
  print(&quot;\n&quot; .. s_xml_tag)  
end

function tap.draw(xml)
end

function tap.reset(xml)
end</code></pre></div><div id="question-tags" class="tags-container tags">xml lua extract tshark soap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '11, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/8eb26411ed8849ab46c314226c598644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sethlwilson&#39;s gravatar image" /><p>sethlwilson<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sethlwilson has one accepted answer">12%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jun '11, 12:41</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-4639" class="comments-container"><span id="4648"></span><div id="comment-4648" class="comment"><div id="post-4648-score" class="comment-score"></div><div class="comment-text"><p>Essentially, using Lua I want to be able to send to output the re-assembled xml like in the Wireshark GUI. It seems like this should be possible given the xml protocol exists right? How else would the GUI do it?</p></div><div id="comment-4648-info" class="comment-info"><span class="comment-age">(21 Jun '11, 09:58)</span> sethlwilson</div></div></div><div id="comment-tools-4639" class="comment-tools"></div><div class="clear"></div><div id="comment-4639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

12 Answers:

</div>

</div>

<span class="curr this_page">1</span><a href="/questions/4639/extracting-soap-xml-payload?sort=votes&amp;page=2" class="page">2</a><span class="next">[next »](/questions/4639/extracting-soap-xml-payload?sort=votes&page=2 "next page")</span>

<span id="4835"></span>

<div id="answer-container-4835" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4835-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Here's Lua that extracts the XML fields to a file (with a dotted line in between fields). I tested it against your pcap in tshark and Wireshark. For tshark, run: <strong><code>tshark -r sethwilson.pcap -R "tcp and data"</code></strong></p><p>Note that the file is written in append mode to:</p><ul><li><strong>UN*X</strong>: <code>~/.wireshark/temp.xml</code></li><li><strong>Windows XP</strong>: <code>C:\Documents and Settings\your_username\Application Data\Wireshark\temp.xml</code></li></ul><hr /><pre><code>-- tap uses dfilter for tcp data and ignores retransmissions
local tap       = Listener.new(nil, &quot;tcp &amp;&amp; data &amp;&amp; !tcp.analysis.retransmission&quot;)
local xml_field = Field.new(&quot;data&quot;)
local file      = nil

-- #######################################################################
-- # If not already open, this opens a file for writing (append mode)
-- #######################################################################
local function open_file()
    if not file then
        local path = USER_DIR .. &quot;/temp.xml&quot;

        print(&quot;opening file:&quot;, path)
        file = assert(io.open(path, &quot;a&quot;), 
                    &quot;Can&#39;t open file for writing&quot;)
    end
end

local HTML_REQ = {
    [&quot;HTTP&quot;] = 1,
    [&quot;GET &quot;] = 1,
    [&quot;PUT &quot;] = 1,
    [&quot;POST&quot;] = 1,
}

-- #######################################################################
-- # Extracts the XML field from the buffer and writes the field to file
-- #######################################################################
local function handle_xml(pinfo, tvb)
    if not file then
        print(&quot;no file...ignoring packet&quot;)
        return
    end

    local fieldinfo = xml_field()
    local xmldata   = tvb(fieldinfo.offset):string()

    -- some of these packets start w/HTTP header...skip to XML
    local starts = xmldata:sub(1,4)
    if HTML_REQ[starts] ~= nil then
        local pos = string.find(xmldata, &quot;&lt;%?xml version&quot;)
        if not pos then
            return
        end

        xmldata = xmldata:sub(pos)
    end

    print(xmldata)
    print(&quot;\n\n-- #&quot;..pinfo.number..&quot; ---------------------------------------------------\n\n&quot;)

    file:write(xmldata)
    file:write(&quot;\n\n-- #&quot;..pinfo.number..&quot; ---------------------------------------------------\n\n&quot;)
end

-- #######################################################################
-- # tap.packet() is called to notify the Listener of a packet that
-- # matches its filter rule (&quot;xml&quot; in this case). This can be called
-- # multiple times before tap.draw().
-- #######################################################################
function tap.packet(pinfo, tvb)
    print(&quot;tap.packet&quot;, &quot;#&quot;..pinfo.number)

    -- XXX: Compensate for no tap.reset() in tshark
    if not gui_enabled() then open_file() end

    -- wrap the handler in a pcall() in case an error occurs
    local ok, msg = pcall(  function() 
                                handle_xml(pinfo,tvb) 
                            end )

    -- print any error and bow out
    if not ok then
        print(&quot;wtf!&quot;, msg)
    end

end

-- #######################################################################
-- # tap.draw() is called to notify the Listener to &quot;draw&quot; its results
-- # that were accumulated in tap.packet(). This is normally called after
-- # tap.packet(), based on &quot;Preferences &gt; Statistics &gt; Tap update interval&quot;.
-- #######################################################################
function tap.draw()
    print(&quot;tap.draw&quot;)

    -- flush toilet (NOTE: When $file is garbage collected, it&#39;s 
    -- automatically flushed and closed...that doesn&#39;t mean we
    -- can&#39;t do it sooner to free resources.)
    if file then
        print(&quot;closing file&quot;)
        file:close()
        file = nil
    end
end

-- #######################################################################
-- # tap.reset() is called to notify the Listener to reset any variables
-- # or counters in preparation for a packet (passed to tap.packet()).
-- # This can be called multiple times before a packet is even seen.
-- #
-- # XXX: tshark doesn&#39;t call this function, but Wireshark does. Bug?
-- #######################################################################
function tap.reset()
    print(&quot;tap.reset&quot;)
    open_file()
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '11, 20:10</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Sep '11, 12:40</p></div></div><div id="comments-container-4835" class="comments-container"><span id="18040"></span><div id="comment-18040" class="comment"><div id="post-18040-score" class="comment-score"></div><div class="comment-text"><p>Great piece of code but unfortunately it fails to extract SOAP message if it was distributed over several TCP segments. Anyone can help to solve this issue?</p></div><div id="comment-18040-info" class="comment-info"><span class="comment-age">(29 Jan '13, 09:07)</span> masgad</div></div></div><div id="comment-tools-4835" class="comment-tools"></div><div class="clear"></div><div id="comment-4835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4861"></span>

<div id="answer-container-4861" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4861-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well we seem to be getting somewhere now -- the complete XML is printed but by bits and pieces over several packets. Here's the output - <a href="http://files.me.com/sethlwilson/vlrmhm">files.me.com/sethlwilson/vlrmhm</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '11, 11:04</strong></p><img src="https://secure.gravatar.com/avatar/8eb26411ed8849ab46c314226c598644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sethlwilson&#39;s gravatar image" /><p>sethlwilson<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sethlwilson has one accepted answer">12%</span></p></div></div><div id="comments-container-4861" class="comments-container"><span id="4865"></span><div id="comment-4865" class="comment"><div id="post-4865-score" class="comment-score"></div><div class="comment-text"><p>By the way the Web services whose traffic I captured (with filter "tcp port 8280") communicates on port 8280.</p></div><div id="comment-4865-info" class="comment-info"><span class="comment-age">(30 Jun '11, 11:10)</span> sethlwilson</div></div><span id="4866"></span><div id="comment-4866" class="comment"><div id="post-4866-score" class="comment-score"></div><div class="comment-text"><p>Yes, exactly. That's the same result I get. We're bypassing TCP reassembly of the HTTP segments, and writing the segments one at a time. If you commented out the dotted lines (debug), you'd get the original payload in the file.</p></div><div id="comment-4866-info" class="comment-info"><span class="comment-age">(30 Jun '11, 11:17)</span> helloworld</div></div><span id="4867"></span><div id="comment-4867" class="comment"><div id="post-4867-score" class="comment-score">1</div><div class="comment-text"><p>Please don't add comments as answers; you should comment on specific posts. Otherwise, this answer list becomes unwieldy and difficult to follow.</p></div><div id="comment-4867-info" class="comment-info"><span class="comment-age">(30 Jun '11, 11:20)</span> helloworld</div></div><span id="4869"></span><div id="comment-4869" class="comment"><div id="post-4869-score" class="comment-score"></div><div class="comment-text"><p>Sorry, no problem and I agree it looks like spaghetti now.<br />
</p><p>So, yes this is now giving me exactly what I've needed! So, does this mean that there is a bug with the TCP reassembly or is it the Lua API? Just wondering if I need to open an artifact.</p><p>Again, thanks for all your help! I was almost to the point of dropping the use of Wireshark in our solution.</p></div><div id="comment-4869-info" class="comment-info"><span class="comment-age">(30 Jun '11, 11:28)</span> sethlwilson</div></div><span id="4871"></span><div id="comment-4871" class="comment"><div id="post-4871-score" class="comment-score"></div><div class="comment-text"><p>One more question ... when I run this script on a live capture, only the request XML is successfully captured. The response appears mangled.</p><p>...</p><p>-- #13 ---------------------------------------------------</p><p>¨:&amp;ó<em>À?A.?q¡f¦qÂ¶˜_øç{ÛÔ,¹üz¹£#áõúçÍÞÖ~«·Éø^</em>DFú›?ÅI£Öðî°™çù?×_ðÀª§tÍ pÎP ¡3Ï5r„"‚b™g$¿ úX;Îæüt(U«‰.…8'˜/Yšàiè­3Ñ!UAåxîý=Ç?ªœv”÷U Ñ(qa9p?Á£á‚+Ÿ¾z„URÒž™í¥¬Tc•” ³3Q;` Å”êë¥-®¤ … ŽDî=Fhr‰²äÑCA&lt;ÚFœBïàïãoóÃ&gt;Æ2ì Üq)Ç+&amp;q‡ëµ‰~Q¨¾,</p><p>-- #19 ---------------------------------------------------</p></div><div id="comment-4871-info" class="comment-info"><span class="comment-age">(30 Jun '11, 12:47)</span> sethlwilson</div></div><span id="4872"></span><div id="comment-4872" class="comment not_top_scorer"><div id="post-4872-score" class="comment-score"></div><div class="comment-text"><p>OK, I think I understand what's going on here - the data in the variable xmldata is gzip compressed. I suppose then that's because we're bypassing the html dissector.</p></div><div id="comment-4872-info" class="comment-info"><span class="comment-age">(30 Jun '11, 13:56)</span> sethlwilson</div></div><span id="4874"></span><div id="comment-4874" class="comment not_top_scorer"><div id="post-4874-score" class="comment-score"></div><div class="comment-text"><p>I doubt the bug is in TCP reassembly because the GUI has no trouble identifying the HTTP/XML packets. My <em>guess</em> is the bug lies in the Lua API (based on the fact that <code>fieldinfo.value</code> and <code>fieldinfo.len</code> do not always correspond to the actual contents of <code>tvb</code>).</p><p>Sure, you're welcome! Helping you only helped me better understand how listeners work, which will help me when I start documenting it the <a href="http://wiki.wireshark.org/LuaAPI">Lua API wiki</a> (an ongoing project).</p></div><div id="comment-4874-info" class="comment-info"><span class="comment-age">(30 Jun '11, 16:31)</span> helloworld</div></div><span id="4875"></span><div id="comment-4875" class="comment not_top_scorer"><div id="post-4875-score" class="comment-score"></div><div class="comment-text"><p>If Wireshark can determine that <code>xml.data</code> is GZIP'ed, then I presume you can write it into a <code>.gz</code> file for later decompression. I think you'd have to pay mind to <code>http.content_length_header</code> to determine the full/expected length of the file.</p></div><div id="comment-4875-info" class="comment-info"><span class="comment-age">(30 Jun '11, 16:39)</span> helloworld</div></div></div><div id="comment-tools-4861" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-4861-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4640"></span>

<div id="answer-container-4640" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4640-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For some reason, I had problems combining the proto variable function call along with the tostring() call So I broke them up and added a check in between.</p><pre><code>On your line:
  local s_xml_cdata = tostring(xml_cdata_f())
try changing to
  local l_xml_cdata = f_xml_cdata()
  if l_xml_cdata == nil then return end
  s_xml_cdata = tostring(l_xml_cdata)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '11, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/6d70926a09a65b1329fb803549ab7205?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NewbieBrian&#39;s gravatar image" /><p>NewbieBrian<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NewbieBrian has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-4640" class="comments-container"><span id="4645"></span><div id="comment-4645" class="comment"><div id="post-4645-score" class="comment-score"></div><div class="comment-text"><p>I tried what you suggested, but the print function doesn't display all of what should be contained in xml.cdata. It appears to be truncating the string.</p></div><div id="comment-4645-info" class="comment-info"><span class="comment-age">(21 Jun '11, 07:29)</span> sethlwilson</div></div><span id="4649"></span><div id="comment-4649" class="comment"><div id="post-4649-score" class="comment-score"></div><div class="comment-text"><p>The middle display area of Wireshark has about 255 character limit. Truncation is correct. I transform the XML entities back to XML characters, then break up the line by carriage return line feeds, returning an array. I print out the array and I get CDATA files of over 750K pretty printing inside WireShark. I can post an example later.</p></div><div id="comment-4649-info" class="comment-info"><span class="comment-age">(21 Jun '11, 11:12)</span> NewbieBrian</div></div></div><div id="comment-tools-4640" class="comment-tools"></div><div class="clear"></div><div id="comment-4640-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4650"></span>

<div id="answer-container-4650" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4650-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>XML CDATA is often encoded with <code>&amp;lt; (&lt;) &amp;gt; (&gt;)</code> and other codes. There may be a better way to do all that follows with an XML parser, but I spend enough time just getting Wireshark to behave as advertised. I don't have time to dive into Lua nuances. So I manually transfer the CDATA to a string as shown above. Then I use string.gsub() to do searches and replaces:</p><pre><code>s_xml_cdata = string.gsub(s_xml_cdata, &quot;&amp;lt;&quot;, &quot;&lt;&quot;)
s_xml_cdata = string.gsub(s_xml_cdata, &quot;&amp;gt;&quot;, &quot;&gt;&quot;)
s_xml_cdata = string.gsub(s_xml_cdata, &quot;&amp;#xA;&quot;, &quot;&quot;)
s_xml_cdata = string.gsub(s_xml_cdata, &quot;&amp;#xD;&quot;, &quot;&quot;)
s_xml_cdata = string.gsub(s_xml_cdata, &quot;\n&quot;, &quot;&quot;)
local la_cdata = BreakUpLongLines(s_xml_cdata, &quot;&gt;&quot;)</code></pre><p>This last line is a call to my function <code>BreakUpLongLines(string_xml_cdata, string split_character)</code>. Pass in your string with the reformed XML data, and the character you want to do splits on. In this case, it's basically the greater than symbol. Here is the BreakUpLongLines() function.</p><pre><code>--utility to break up long lines into smaller ones
function BreakUpLongLines (str, sep)
    --Array to return each of the elements
    vals = {}; valindex = 1; word = &quot;&quot;
    local strSize = #str
    local offset =0
    while strSize &gt; offset do
        svar, evar=string.find(str, sep, offset)
        if evar == nil then return vals end
        if evar &gt; strSize then return vals end
        vals[valindex] = string.sub(str, offset,evar)
        valindex = valindex+1
        offset=evar+1
    end
    return vals
end</code></pre><p>So this function will take any long line and break it by the sep character, which for XML happens to be the greater than symbol. It returns an array of all your lines. Use a simple For loop to print your lines.</p><pre><code>for kvar,vvar in next, la_cdata do
    g2stree:add(kvar, la_cdata[kvar])
end</code></pre><p>Comments and improvements welcome!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '11, 11:28</strong></p><img src="https://secure.gravatar.com/avatar/6d70926a09a65b1329fb803549ab7205?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NewbieBrian&#39;s gravatar image" /><p>NewbieBrian<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NewbieBrian has no accepted answers">0%</span></p></div></div><div id="comments-container-4650" class="comments-container"><span id="4656"></span><div id="comment-4656" class="comment"><div id="post-4656-score" class="comment-score"></div><div class="comment-text"><p>Ok, but this doesn't solve the original problem, which is to grab the entire XML document.</p></div><div id="comment-4656-info" class="comment-info"><span class="comment-age">(21 Jun '11, 18:03)</span> helloworld</div></div></div><div id="comment-tools-4650" class="comment-tools"></div><div class="clear"></div><div id="comment-4650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4651"></span>

<div id="answer-container-4651" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4651-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I do appreciate your help. Here is my latest rendition incorporating your latest suggestion. The file:write(s_xml_cdata) prints only 4 bytes of the xml, and that data is the value contained in the first set of tags. I'm running this with tshark using the following command: tshark -f "tcp port 8280" -X lua_script:C:Userssetwilxml.lua. My service is going over that port specifically. I have the following Wireshark packaage installed:</p><p>Version 1.6.0 (SVN Rev 37592 from /trunk-1.6)</p><p>Copyright 1998-2011 Gerald Combs [email protected] and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with GTK+ 2.22.1, with GLib 2.26.1, with WinPcap (version unknown), with libz 1.2.5, without POSIX capabilities, without libpcre, without SMI, with c-ares 1.7.1, with Lua 5.1, without Python, with GnuTLS 2.10.3, with Gcrypt 1.4.6, without Kerberos, with GeoIP, with PortAudio V19-devel (built Jun 7 2011), with AirPcap.</p><p>Running on 64-bit Windows 7, build 7600, with WinPcap version 4.1.2 (packet.dll version 4.1.0.2001), based on libpcap version 1.0 branch 1_0_rel0b (20091008), GnuTLS 2.10.3, Gcrypt 1.4.6, without AirPcap.</p><p>Built using Microsoft Visual C++ 9.0 build 21022</p><pre><code>do
  local file = io.open(&quot;C:\\Users\\setwil\\xml.out&quot;, &quot;w&quot;)

  f_xml_cdata = Field.new(&quot;xml.cdata&quot;)

  --utility to break up long lines into smaller ones
  function BreakUpLongLines (str, sep)
    --Array to return each of the elements
    vals = {}; valindex = 1; word = &quot;&quot;
    local strSize = #str
    local offset =0
    print(&quot;\nstrSize=&quot; .. strSize .. &quot;\n&quot;)
    while strSize &gt; offset do
        svar, evar=string.find(str, sep, offset)
        if evar == nil then return vals end
        if evar &gt; strSize then return vals end
        vals[valindex] = string.sub(str, offset,evar)
        valindex = valindex+1
        offset=evar+1
    end
    return vals
  end

  local mytap = Listener.new(nil, &quot;xml&quot;)

  function mytap.packet(pinfo, tvb, xml)

    local l_xml_cdata = f_xml_cdata()
    local s_xml_cdata = tostring(l_xml_cdata)

    s_xml_cdata = string.gsub(s_xml_cdata, &quot;&amp;lt;&quot;, &quot;&lt;&quot;)
    s_xml_cdata = string.gsub(s_xml_cdata, &quot;&amp;gt;&quot;, &quot;&gt;&quot;)
    s_xml_cdata = string.gsub(s_xml_cdata, &quot;&amp;#xA;&quot;, &quot;&quot;)
    s_xml_cdata = string.gsub(s_xml_cdata, &quot;&amp;#xD;&quot;, &quot;&quot;)
    s_xml_cdata = string.gsub(s_xml_cdata, &quot;\n&quot;, &quot;&quot;)

    file:write(s_xml_cdata)

    local la_cdata = BreakUpLongLines(s_xml_cdata, &quot;&gt;&quot;)

    file:write(&quot;\nBefore loop&quot;)
    for i,v in ipairs(la_cdata), la_cdata do
      file:write(v)
    end
    file:write(&quot;\nAfter loop&quot;)

  end

  function mytap.draw()
  end

  function mytap.reset()
    file:close()
  end
end</code></pre></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '11, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/8eb26411ed8849ab46c314226c598644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sethlwilson&#39;s gravatar image" /><p>sethlwilson<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sethlwilson has one accepted answer">12%</span></p></div></div><div id="comments-container-4651" class="comments-container"></div><div id="comment-tools-4651" class="comment-tools"></div><div class="clear"></div><div id="comment-4651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4657"></span>

<div id="answer-container-4657" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4657-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To dump XML documents from a tap/listener:</p><pre><code>local tap = Listener.new(nil, &quot;xml&quot;)
local xml_field = Field.new(&quot;xml&quot;)

function tap.packet (pinfo, tvb)

    -- Extract the XML field (which contains the full XML document).
    --
    -- NOTE: `xml_field()` returns a `FieldInfo` object. See this link for more info:
    -- http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Field.html#lua_class_FieldInfo

    local fieldinfo = xml_field()

    -- `print()` refuses to print the field because it &quot;may contain invalid
    -- characters&quot;. The particular subfield that&#39;s causing the problem is
    -- `fieldinfo.label` (not sure why). One would think that `fieldinfo.value`
    -- would contain the full XML and `fieldinfo.len` would be the document&#39;s
    -- byte length, but not true (bug?).
    -- 
    -- No worries. We can parse the string from the `tvb` ourselves. `fieldinfo.offset`
    -- tells us where in the `tvb` the XML document begins. So, all we need to do
    -- is convert the bytes from the offset to the end of the buffer into a string.
    -- (This assumes that the XML document is the last field in the packet.)
    --
    -- See http://wiki.wireshark.org/LuaAPI/Tvb#tvbrange:string.28.29

    print( tvb(fieldinfo.offset):string() )
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '11, 18:10</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-4657" class="comments-container"></div><div id="comment-tools-4657" class="comment-tools"></div><div class="clear"></div><div id="comment-4657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4671"></span>

<div id="answer-container-4671" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4671-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks helloworld, now I'm getting somewhere! Funny thing though is that using the code below I only get a portion of the xml and the amount differs between the request and the response. I confirmed though that the offset given by the FieldInfo object is the same as that indicated in the Wireshark GUI. Do you think that there may be some stray non-printable characters in the tvb that are interfering with string conversion? Again I'm running this with tshark from cmd.exe.</p><pre><code>local tap = Listener.new(nil, &quot;xml&quot;)
local xml_field = Field.new(&quot;xml&quot;)
local file = io.open(&quot;C:\\Users\\setwil\\xml.out&quot;, &quot;w&quot;)

function tap.packet(pinfo, tvb)
  local fieldinfo = xml_field() 
  print(&quot;fieldinfo.name=&quot; .. tostring(fieldinfo.name))
  print(&quot;fieldinfo.len=&quot; .. tostring(fieldinfo.len))
  print(&quot;fieldinfo.offset=&quot; .. tostring(fieldinfo.offset))
  --print(&quot;fieldinfo.value=&quot; .. tostring(fieldinfo.value))

  file:write( tvb(fieldinfo.offset):string() )
  file:write(&quot;\n------------------------------------------------------------\n\n&quot;)

end

function tap.reset()
  file:close()
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '11, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/8eb26411ed8849ab46c314226c598644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sethlwilson&#39;s gravatar image" /><p>sethlwilson<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sethlwilson has one accepted answer">12%</span></p></div></div><div id="comments-container-4671" class="comments-container"><span id="4676"></span><div id="comment-4676" class="comment"><div id="post-4676-score" class="comment-score"></div><div class="comment-text"><p>Something that I've just discovered is that for one packet that I captured, the fieldinfo.offset is greater than the tvb:len(). Here's the program output:</p><p>fieldinfo.name=xml</p><p>fieldinfo.len=6068</p><p>fieldinfo.offset=257</p><p>fieldinfo.range=3c736f6170656e763a456e76656c6f706520786d6c6e733a...</p><p>fieldinfo.generated=false</p><p>tvb:length=282</p><p>So it leaves me wondering to what buffer fieldinfo.offset refers.</p></div><div id="comment-4676-info" class="comment-info"><span class="comment-age">(22 Jun '11, 13:04)</span> sethlwilson</div></div><span id="4680"></span><div id="comment-4680" class="comment"><div id="post-4680-score" class="comment-score"></div><div class="comment-text"><p>An additional discovery: When comparing these results with those of the GUI I discovered that what's contained in tvb are the bytes from the <em>frame</em> and that its contents are what's printing to my file.</p></div><div id="comment-4680-info" class="comment-info"><span class="comment-age">(22 Jun '11, 14:32)</span> sethlwilson</div></div><span id="4713"></span><div id="comment-4713" class="comment"><div id="post-4713-score" class="comment-score"></div><div class="comment-text"><p>I guess the non-printable chars theory is plausible. Isn't that discernible from the hexdump in Wireshark/tshark?</p><p>The <code>fieldinfo.offset</code> field is the raw offset from the beginning of the frame. I'm not sure why <code>fieldinfo.len</code> and <code>tvb:length</code> are so different.</p><p>Do you have a pcap to share (or a way for me to recreate your symptoms)?</p></div><div id="comment-4713-info" class="comment-info"><span class="comment-age">(23 Jun '11, 19:46)</span> helloworld</div></div><span id="4726"></span><div id="comment-4726" class="comment"><div id="post-4726-score" class="comment-score"></div><div class="comment-text"><p>Sure I can share the pcap with you. How can I send it to you?</p></div><div id="comment-4726-info" class="comment-info"><span class="comment-age">(24 Jun '11, 06:42)</span> sethlwilson</div></div><span id="4746"></span><div id="comment-4746" class="comment"><div id="post-4746-score" class="comment-score"></div><div class="comment-text"><p>You can share the pcap via <a href="http://min.us/">min.us</a>, and post a link here to it.</p></div><div id="comment-4746-info" class="comment-info"><span class="comment-age">(24 Jun '11, 16:18)</span> helloworld</div></div><span id="4769"></span><div id="comment-4769" class="comment not_top_scorer"><div id="post-4769-score" class="comment-score"></div><div class="comment-text"><p>Here is the pcap file in question: http://files.me.com/sethlwilson/cd4tw7</p></div><div id="comment-4769-info" class="comment-info"><span class="comment-age">(27 Jun '11, 09:02)</span> sethlwilson</div></div></div><div id="comment-tools-4671" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-4671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4739"></span>

<div id="answer-container-4739" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4739-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, I finally managed to obtain the XML payload using the below approach which probably isn't too terribly efficient. During a live capture I capture a single request-response relay and print their soap envelope contents. As for the request, I get all of the xml, byte for byte; but as for the response, there are some bytes missing at the very end of the xml:</p><pre><code>... 
&lt;/Response&gt;
&lt;SubClientID&gt;MAS01&lt;/SubClientID&gt;
&lt;UserID&gt;PSPRPC1&lt;/UserID&gt;
&lt;/APPX&gt;
&lt;/ns:getAPPXResponse&gt;
&lt;/SOAP-ENV:Bod</code></pre><p>The missing bytes are ...</p><pre><code>y&gt;
&lt;/SOAP-ENV:Envelope&gt;</code></pre><p>At first I thought I was unintentionally lopping off those bytes in my convoluted algorithm, but in fact those bytes are even missing in xml_fieldinfo.value ( xml_fieldinfo.len / 2 == string.length(xml_string) ).</p><p>Why would the value member be truncated? Do you think that it's a bug, or is it an imposed limit?</p><p>Program source:</p><pre><code>local tap = Listener.new(nil, &quot;xml&quot;)
local xml_field = Field.new(&quot;xml&quot;)
local file = io.open(&quot;C:\\Users\\setwil\\xml.out&quot;, &quot;w&quot;)

function tap.packet(pinfo, tvb)
  local xml_fieldinfo = xml_field()  
  local xml_hex_string = tostring(xml_fieldinfo.value)
  print(&quot;xml_fieldinfo.len&quot; .. xml_fieldinfo.len .. &quot;\n\n&quot;)
  file:write(&quot;xml_hex_string=&quot; .. &quot;\n&quot; .. xml_hex_string .. &quot;\n\n&quot;)
  print(&quot;xml_hex_string.length=&quot; .. string.len(xml_hex_string) .. &quot;\n&quot;)

  local xml_string

  for i = 1, string.len(xml_hex_string), 2 do
    local hex_byte = string.sub(xml_hex_string, i, (i + 1))

    if( i == 1 ) then
      xml_string = string.char(tonumber(hex_byte, 16))
    else
      xml_string = xml_string .. string.char(tonumber(hex_byte, 16))
    end

  end

  file:write(xml_string .. &quot;\n\n&quot;)
  file:write(&quot;---------------------------------------------------------------\n\n&quot;)  
end

function tap.reset()
  file:close()
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '11, 12:54</strong></p><img src="https://secure.gravatar.com/avatar/8eb26411ed8849ab46c314226c598644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sethlwilson&#39;s gravatar image" /><p>sethlwilson<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sethlwilson has one accepted answer">12%</span></p></div></div><div id="comments-container-4739" class="comments-container"><span id="4836"></span><div id="comment-4836" class="comment"><div id="post-4836-score" class="comment-score"></div><div class="comment-text"><p>Yes, I think it's a bug that <code>xml_fieldinfo.value</code> is missing bytes (and I had commented that in the example code of my earlier answer). Skimming the internal code, I don't see an imposed limit, so we shouldn't be seeing this.</p></div><div id="comment-4836-info" class="comment-info"><span class="comment-age">(29 Jun '11, 21:16)</span> helloworld</div></div></div><div id="comment-tools-4739" class="comment-tools"></div><div class="clear"></div><div id="comment-4739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4819"></span>

<div id="answer-container-4819" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4819-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Here is the pcap file in question: <a href="http://files.me.com/sethlwilson/cd4tw7">http://files.me.com/sethlwilson/cd4tw7</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '11, 12:22</strong></p><img src="https://secure.gravatar.com/avatar/8eb26411ed8849ab46c314226c598644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sethlwilson&#39;s gravatar image" /><p>sethlwilson<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sethlwilson has one accepted answer">12%</span></p></div></div><div id="comments-container-4819" class="comments-container"></div><div id="comment-tools-4819" class="comment-tools"></div><div class="clear"></div><div id="comment-4819-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4844"></span>

<div id="answer-container-4844" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4844-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi helloworld,</p><p>I tried your Lua program, but I'm not getting any output (temp.xml is never created) when replaying my pcap. Tap.packet() never fires.</p><pre><code>C:\Program Files\Wireshark&gt;tshark -r C:\Users\setwil\sethwilson.pcap -R &quot;tcp and data&quot; -X lua_script:C:\Users\setwil\helloworld_xml_sniff_devl.lua
tap.draw

C:\Program Files\Wireshark&gt;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '11, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/8eb26411ed8849ab46c314226c598644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sethlwilson&#39;s gravatar image" /><p>sethlwilson<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sethlwilson has one accepted answer">12%</span></p></div></div><div id="comments-container-4844" class="comments-container"><span id="4846"></span><div id="comment-4846" class="comment"><div id="post-4846-score" class="comment-score"></div><div class="comment-text"><p>Something is wrong with your cmdline entry (try quotes around the path of -r). It works for me on OSX and XP.</p></div><div id="comment-4846-info" class="comment-info"><span class="comment-age">(30 Jun '11, 08:11)</span> helloworld</div></div><span id="4849"></span><div id="comment-4849" class="comment"><div id="post-4849-score" class="comment-score"></div><div class="comment-text"><p>Another possible problem is that a dissector is parsing out your TCP data (as HTTP?), which could cause the tap's filter to miss the packets. If so, you'd have to either change the tap filter or disable the custom dissector. If it's just HTTP, then change both the tap filter and the field name to "xml".</p></div><div id="comment-4849-info" class="comment-info"><span class="comment-age">(30 Jun '11, 08:32)</span> helloworld</div></div><span id="4850"></span><div id="comment-4850" class="comment"><div id="post-4850-score" class="comment-score"></div><div class="comment-text"><p>I just reproduced the symptom. In my case, my HTTP prefs did not include 56013 as an HTTP port, so these packets were falling thru as undissected data (allowing for "tcp and data" filter to catch them). Try the filter/fieldname change I previously mentioned.</p></div><div id="comment-4850-info" class="comment-info"><span class="comment-age">(30 Jun '11, 08:43)</span> helloworld</div></div></div><div id="comment-tools-4844" class="comment-tools"></div><div class="clear"></div><div id="comment-4844-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

<span class="curr this_page">1</span><a href="/questions/4639/extracting-soap-xml-payload?sort=votes&amp;page=2" class="page">2</a><span class="next">[next »](/questions/4639/extracting-soap-xml-payload?sort=votes&page=2 "next page")</span>

</div>

</div>

</div>

