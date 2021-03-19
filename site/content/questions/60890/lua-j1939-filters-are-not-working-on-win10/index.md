+++
type = "question"
title = "Lua J1939 filters are not working on Win10"
description = '''ON a MAC, I am using Wireshark (tshark.exe) to do som CAN - J1939 filtering. I have done it with a script in LUA. This is working fine. But when I try it in Win10, I have problems by doing the field.new on a j1939 This is part of my LUA file. j1939_src = Field.new(&quot;j1939.src_addr&quot;) src = tostring(j1...'''
date = "2017-04-19T07:55:00Z"
lastmod = "2017-05-04T04:47:00Z"
weight = 60890
keywords = [ "j1939", "can", "lua" ]
aliases = [ "/questions/60890" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua J1939 filters are not working on Win10](/questions/60890/lua-j1939-filters-are-not-working-on-win10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60890-score" class="post-score" title="current number of votes">0</div><span id="post-60890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>ON a MAC, I am using Wireshark (tshark.exe) to do som CAN - J1939 filtering. I have done it with a script in LUA.</p><p>This is working fine.</p><p>But when I try it in Win10, I have problems by doing the field.new on a j1939</p><p>This is part of my LUA file.</p><pre><code>j1939_src = Field.new(&quot;j1939.src_addr&quot;)
src = tostring(j1939_src())</code></pre><p>In the line:</p><pre><code>src = tostring(j1939_src())</code></pre><p>I get the error</p><pre><code>tshark: Lua: on packet 1 Error During execution of Listener Packet Callback:
[string &quot;scan_varids.lua&quot;]:58: bad argument #1 to &#39;tostring&#39; (value expected)</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-j1939" rel="tag" title="see questions tagged &#39;j1939&#39;">j1939</span> <span class="post-tag tag-link-can" rel="tag" title="see questions tagged &#39;can&#39;">can</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '17, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/ee6ea3ad5c8ead434d53569b0b3673a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Klaus%20Jakobsen&#39;s gravatar image" /><p><span>Klaus Jakobsen</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Klaus Jakobsen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 May '17, 06:38</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-60890" class="comments-container"><span id="60892"></span><div id="comment-60892" class="comment"><div id="post-60892-score" class="comment-score">1</div><div class="comment-text"><p>While this may not be your issue, when comparing two different builds of Wireshark it's helpful to state the version numbers of the two versions.</p></div><div id="comment-60892-info" class="comment-info"><span class="comment-age">(19 Apr '17, 10:59)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="60904"></span><div id="comment-60904" class="comment"><div id="post-60904-score" class="comment-score"></div><div class="comment-text"><p>On my MAC it is Wireshark 2.2.1. On my Win10 I tried initially with newest (2.2.6) but to be sure I also tried the 2.2.1 on my Win10. It is the same. Both win installations are not working ane are giving the same error.</p></div><div id="comment-60904-info" class="comment-info"><span class="comment-age">(19 Apr '17, 23:58)</span> <span class="comment-user userinfo">Klaus Jakobsen</span></div></div><span id="60908"></span><div id="comment-60908" class="comment"><div id="post-60908-score" class="comment-score">1</div><div class="comment-text"><p>Can you post the full contents of your Lua script.</p></div><div id="comment-60908-info" class="comment-info"><span class="comment-age">(20 Apr '17, 00:35)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="60909"></span><div id="comment-60909" class="comment"><div id="post-60909-score" class="comment-score"></div><div class="comment-text"><pre><code>--Househam boom LHS (PWM in Test &amp; dianostic)
filter_test = { &quot;master volt&quot;, &quot;slave volt&quot;, &quot;tractor volt&quot;, &quot;fule level&quot;, &quot;rpm inc&quot;, &quot;speed&quot;, &quot;dis count&quot;, &quot;max gear&quot;, &quot;trans type&quot;, &quot;engine houers on tractor&quot;, &quot;break press&quot;, &quot;RPM&quot;, &quot;test speed&quot; }
filter_varids = { 284, 285, 286, 201, 105, 1, 44, 807, 1153, 321, 1204, 5, 256 }

-- Udvælg J1939 felter
tap = Listener.new(&quot;frame&quot;)
frame_time = Field.new(&quot;frame.time_relative&quot;)
j1939_src = Field.new(&quot;j1939.src_addr&quot;)
j1939_dst = Field.new(&quot;j1939.dst_addr&quot;)
j1939_canid = Field.new(&quot;j1939.can_id&quot;)
j1939_pgn = Field.new(&quot;j1939.pgn&quot;)
j1939_data = Field.new(&quot;j1939.data&quot;)

-- Udskriv CSV header og beregn kolonnenummer for hver varid
varids_to_columns = {}
column_count = 0

io.write(&quot;Time;&quot;)
for i, varid in ipairs(filter_varids) do 
  column_count = column_count + 1
  varids_to_columns[varid] = column_count
  io.write(filter_test[i] .. &quot; (&quot; .. varid .. &quot;);&quot;) 
end
io.write(&quot;\n&quot;)

-- Gennemgå alle pakkerne
function tap.packet (pinfo,tvb,ip)
  time = tostring(frame_time())
  src = tostring(j1939_src())
  canid = tostring(j1939_canid())
  pgn = tostring(j1939_pgn())
  data = tostring(j1939_data()):gsub(&quot;:&quot;, &quot;&quot;):fromhex()
  var_id = 0;
  var_value = 0;

  if pgn == &quot;126720&quot; or pgn == &quot;61184&quot; then -- Proprietary A or A2
    if u8(data,0) == 0x25 then -- VarID
      var_id = u16(data, 2)
      if var_id &gt;3900 then  -- if test VAR_ids
        var_value = u16(data, 6)
      else
        var_value = s32(data, 4)
      end

      -- Check om varid&#39;en er en af dem vi skal kigge på
      if varids_to_columns[var_id] then
          io.write(time:gsub(&quot;%.&quot;, &quot;,&quot;)) -- Erstat punktum med komma i tidsstempel for at Excel forstår det
          -- Udskriv semikolonner indtil vi når den kolonne, vi skal have værdien ind på
          for i=1, varids_to_columns[var_id], 1 do
      io.write( &quot;;&quot; )
          end
    io.write( var_value .. &quot;\n&quot; )
        end
    end
  end

--  if src == &quot;9&quot; then -- Vi ser kun på beskeder fra CAN-ID 9
--      io.write( &quot;VarID: \n&quot; )
--  end
end</code></pre></div><div id="comment-60909-info" class="comment-info"><span class="comment-age">(20 Apr '17, 01:05)</span> <span class="comment-user userinfo">Klaus Jakobsen</span></div></div><span id="60910"></span><div id="comment-60910" class="comment"><div id="post-60910-score" class="comment-score"></div><div class="comment-text"><pre><code>-- DIVERSE HJÆLPEFUNKTIONER
function string.fromhex(str)
    return (str:gsub(&#39;..&#39;, function (cc)
        return string.char(tonumber(cc, 16))
    end))
end

function string.tohex(str)
    return (str:gsub(&#39;.&#39;, function (c)
        return string.format(&#39;%02X&#39;, string.byte(c))
    end))
end

--- Get an 8-bit integer at a 0-based byte offset in a byte string.
-- @param b A byte string.
-- @param i Offset.
-- @return An 8-bit integer.
function u8(b, i)
  return string.byte(b, i+1)
end

--- Get a 16-bit integer at a 0-based byte offset in a byte string.
-- @param b A byte string.
-- @param i Offset.
-- @return A 16-bit integer.
function u16(b, i)
  local b1,b2
  b1, b2 = string.byte(b, i+1), string.byte(b, i+2)
  --        2^8     2^0
  return b1*256 + b2
end

--- Get a 32-bit integer at a 0-based byte offset in a byte string.
-- @param b A byte string.
-- @param i Offset.
-- @return A 32-bit integer.
function u32(b,i)
  local b1,b2,b3,b4
  b1, b2 = string.byte(b, i+1), string.byte(b, i+2)
  b3, b4 = string.byte(b, i+3), string.byte(b, i+4)
  --        2^24          2^16       2^8     2^0
  return b1*16777216 + b2*65536 + b3*256 + b4
end

--- Get a 32-bit integer at a 0-based byte offset in a byte string.
-- @param b A byte string.
-- @param i Offset.
-- @return A 32-bit signed integer.
function s32(b,i)
  local b1,b2,b3,b4
  b1, b2 = string.byte(b, i+1), string.byte(b, i+2)
  b3, b4 = string.byte(b, i+3), string.byte(b, i+4)
  --        2^24          2^16       2^8     2^0
  b = b1*16777216 + b2*65536 + b3*256 + b4
  if b &gt;= 2^31 then
    return b - 2^32
  else
    return b
  end
end</code></pre></div><div id="comment-60910-info" class="comment-info"><span class="comment-age">(20 Apr '17, 01:06)</span> <span class="comment-user userinfo">Klaus Jakobsen</span></div></div><span id="60911"></span><div id="comment-60911" class="comment not_top_scorer"><div id="post-60911-score" class="comment-score"></div><div class="comment-text"><p>This is not nice. Is it possible to add a file instead</p></div><div id="comment-60911-info" class="comment-info"><span class="comment-age">(20 Apr '17, 01:07)</span> <span class="comment-user userinfo">Klaus Jakobsen</span></div></div><span id="60914"></span><div id="comment-60914" class="comment not_top_scorer"><div id="post-60914-score" class="comment-score"></div><div class="comment-text"><p>Use the <code>&lt;pre</code>&gt;<code>&lt;/pre</code>&gt; markup around code.</p></div><div id="comment-60914-info" class="comment-info"><span class="comment-age">(20 Apr '17, 03:47)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="60915"></span><div id="comment-60915" class="comment not_top_scorer"><div id="post-60915-score" class="comment-score"></div><div class="comment-text"><p>First part of the file:</p><pre><code>-- Kommandoer til at starte programmet med:
-- tshark -i Househam_boom_reg_canlog/010-1770571252_bus_1.pcap -X lua_script:hej.lua
-- tshark -q -c10 -r 010-1770571252_bus_1.pcap -X lua_script:hej.lua
-- tshark -q -r 010-1770571252_bus_1.pcap -X lua_script:hej.lua &gt; output.csv
-- VarID&#39;er som skal trækkes frem:
--Househam boom LHS (PWM in Test &amp; dianostic)
filter_test = { &quot;master volt&quot;, &quot;slave volt&quot;, &quot;tractor volt&quot;, &quot;fule level&quot;, &quot;rpm inc&quot;, &quot;speed&quot;, &quot;dis count&quot;, &quot;max gear&quot;, &quot;trans type&quot;, &quot;engine houers on tractor&quot;, &quot;break press&quot;, &quot;RPM&quot;, &quot;test speed&quot; }
filter_varids = { 284, 285, 286, 201, 105, 1, 44, 807, 1153, 321, 1204, 5, 256 }
-- Udvælg J1939 felter
tap = Listener.new(&quot;frame&quot;)
frame_time = Field.new(&quot;frame.time_relative&quot;)
j1939_src = Field.new(&quot;j1939.src_addr&quot;)
j1939_dst = Field.new(&quot;j1939.dst_addr&quot;)
j1939_canid = Field.new(&quot;j1939.can_id&quot;)
j1939_pgn = Field.new(&quot;j1939.pgn&quot;)
j1939_data = Field.new(&quot;j1939.data&quot;)
-- Udskriv CSV header og beregn kolonnenummer for hver varid
varids_to_columns = {}
column_count = 0
io.write(&quot;Time;&quot;)
for i, varid in ipairs(filter_varids) do 
  column_count = column_count + 1
  varids_to_columns[varid] = column_count
  io.write(filter_test[i] .. &quot; (&quot; .. varid .. &quot;);&quot;) 
end
io.write(&quot;\n&quot;)
-- Gennemgå alle pakkerne
function tap.packet (pinfo,tvb,ip)
  time = tostring(frame_time())
  src = tostring(j1939_src())
  canid = tostring(j1939_canid())
  pgn = tostring(j1939_pgn())
  data = tostring(j1939_data()):gsub(&quot;:&quot;, &quot;&quot;):fromhex()
  var_id = 0;
  var_value = 0;
if pgn == &quot;126720&quot; or pgn == &quot;61184&quot; then -- Proprietary A or A2
    if u8(data,0) == 0x25 then -- VarID
      var_id = u16(data, 2)
      if var_id &gt;3900 then  -- if test VAR_ids
        var_value = u16(data, 6)
      else
        var_value = s32(data, 4)
      end
  -- Check om varid&#39;en er en af dem vi skal kigge på
  if varids_to_columns[var_id] then
      io.write(time:gsub(&quot;%.&quot;, &quot;,&quot;)) -- Erstat punktum med komma i tidsstempel for at Excel forstår det
      -- Udskriv semikolonner indtil vi når den kolonne, vi skal have værdien ind på
      for i=1, varids_to_columns[var_id], 1 do
    io.write( &quot;;&quot; )
      end
  io.write( var_value .. &quot;\n&quot; )
    end
end</code></pre><p>end</p><p>-- if src == "9" then -- Vi ser kun på beskeder fra CAN-ID 9 -- io.write( "VarID: \n" ) -- end end</p></pre></div><div id="comment-60915-info" class="comment-info"><span class="comment-age">(20 Apr '17, 03:54)</span> <span class="comment-user userinfo">Klaus Jakobsen</span></div></div><span id="60916"></span><div id="comment-60916" class="comment not_top_scorer"><div id="post-60916-score" class="comment-score"></div><div class="comment-text"><p>Second part of the file</p><pre><code>-- DIVERSE HJÆLPEFUNKTIONER
function string.fromhex(str)
    return (str:gsub(&#39;..&#39;, function (cc)
        return string.char(tonumber(cc, 16))
    end))
end
function string.tohex(str)
    return (str:gsub(&#39;.&#39;, function (c)
        return string.format(&#39;%02X&#39;, string.byte(c))
    end))
end
--- Get an 8-bit integer at a 0-based byte offset in a byte string.
-- @param b A byte string.
-- @param i Offset.
-- @return An 8-bit integer.
function u8(b, i)
  return string.byte(b, i+1)
end
--- Get a 16-bit integer at a 0-based byte offset in a byte string.
-- @param b A byte string.
-- @param i Offset.
-- @return A 16-bit integer.
function u16(b, i)
  local b1,b2
  b1, b2 = string.byte(b, i+1), string.byte(b, i+2)
  --        2^8     2^0
  return b1*256 + b2
end
--- Get a 32-bit integer at a 0-based byte offset in a byte string.
-- @param b A byte string.
-- @param i Offset.
-- @return A 32-bit integer.
function u32(b,i)
  local b1,b2,b3,b4
  b1, b2 = string.byte(b, i+1), string.byte(b, i+2)
  b3, b4 = string.byte(b, i+3), string.byte(b, i+4)
  --        2^24          2^16       2^8     2^0
  return b116777216 + b265536 + b3*256 + b4
end
--- Get a 32-bit integer at a 0-based byte offset in a byte string.
-- @param b A byte string.
-- @param i Offset.
-- @return A 32-bit signed integer.
function s32(b,i)
  local b1,b2,b3,b4
  b1, b2 = string.byte(b, i+1), string.byte(b, i+2)
  b3, b4 = string.byte(b, i+3), string.byte(b, i+4)
  --        2^24          2^16       2^8     2^0
  b = b116777216 + b265536 + b3*256 + b4
  if b &gt;= 2^31 then
    return b - 2^32
  else
    return b
  end
end</code></pre></div><div id="comment-60916-info" class="comment-info"><span class="comment-age">(20 Apr '17, 03:55)</span> <span class="comment-user userinfo">Klaus Jakobsen</span></div></div><span id="60919"></span><div id="comment-60919" class="comment not_top_scorer"><div id="post-60919-score" class="comment-score"></div><div class="comment-text"><p>I am also facing a similar issue with Field.new. LUA script was working in previous wireshark builds, but after updating to 1.12.7 for win7 its now failing. I have checked this field and it does exist. Whats changed?</p><p>[string "GSMMAP.lua"]:244: bad argument #1 to '?' (Field_new: a field with this name must exist)</p><p>tcap_abort = Field.new("tcap.abort_element") --- line 244</p></div><div id="comment-60919-info" class="comment-info"><span class="comment-age">(20 Apr '17, 05:37)</span> <span class="comment-user userinfo">niismail</span></div></div><span id="61205"></span><div id="comment-61205" class="comment not_top_scorer"><div id="post-61205-score" class="comment-score"></div><div class="comment-text"><p>Hi there, would you be able to share a sample capture of the J1939 data?</p></div><div id="comment-61205-info" class="comment-info"><span class="comment-age">(03 May '17, 06:22)</span> <span class="comment-user userinfo">mfcss</span></div></div><span id="61223"></span><div id="comment-61223" class="comment not_top_scorer"><div id="post-61223-score" class="comment-score"></div><div class="comment-text"><p>Hi WIreshark Q&amp;A I have placed a fil in dropbox:</p><p><a href="https://www.dropbox.com/s/oxmxnkyefw2tcs9/010-2129680398_bus_1.pcap?dl=0">https://www.dropbox.com/s/oxmxnkyefw2tcs9/010-2129680398_bus_1.pcap?dl=0</a></p></div><div id="comment-61223-info" class="comment-info"><span class="comment-age">(04 May '17, 01:36)</span> <span class="comment-user userinfo">Klaus Jakobsen</span></div></div><span id="61226"></span><div id="comment-61226" class="comment not_top_scorer"><div id="post-61226-score" class="comment-score"></div><div class="comment-text"><p>Thanks Klaus - in case you happen to have a sample version of the file including some of the more standard/non proprietary PGN data (e.g. wheel speed, RPM, ...) that would be interesting. But otherwise appreciate the sharing of above.</p></div><div id="comment-61226-info" class="comment-info"><span class="comment-age">(04 May '17, 04:47)</span> <span class="comment-user userinfo">mfcss</span></div></div></div><div id="comment-tools-60890" class="comment-tools"><span class="comments-showing"> showing 5 of 13 </span> <a href="#" class="show-all-comments-link">show 8 more comments</a></div><div class="clear"></div><div id="comment-60890-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

