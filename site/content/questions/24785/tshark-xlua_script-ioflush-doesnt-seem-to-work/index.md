+++
type = "question"
title = "tshark, -Xlua_script: io.flush() doesn&#x27;t seem to work"
description = '''io.flush doesn&#x27;t seem to do anything from inside a Lua listener. Concretely, my script looks like this in outline: local ip = Listener.new(&quot;ip&quot;) function ip.packet(pinfo, tvb)  ...  io.write(string.format(&quot;%d:%d:%.6f:%s:%s:%s:%d:%s:%s:%d:%d:%s&#92;n&quot;, ...))  io.flush() end  but output is still being buf...'''
date = "2013-09-16T15:42:00Z"
lastmod = "2013-09-17T07:43:00Z"
weight = 24785
keywords = [ "lua", "tshark" ]
aliases = [ "/questions/24785" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark, -Xlua\_script: io.flush() doesn't seem to work](/questions/24785/tshark-xlua_script-ioflush-doesnt-seem-to-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24785-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24785-score" class="post-score" title="current number of votes">0</div><span id="post-24785-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><code>io.flush</code> doesn't seem to do anything from inside a Lua listener. Concretely, my script looks like this in outline:</p><pre><code>local ip = Listener.new(&quot;ip&quot;)
function ip.packet(pinfo, tvb)
    ...
    io.write(string.format(&quot;%d:%d:%.6f:%s:%s:%s:%d:%s:%s:%d:%d:%s\n&quot;, ...))
    io.flush()
end</code></pre><p>but output is still being buffered. This wouldn't be an issue, except that the <code>tshark</code> process might get killed at any time by higher-level code, and it doesn't seem to flush pending output when it receives <code>SIGTERM</code>.</p><p>Please advise how I can ensure that each and every packet is logged as it comes in.</p><p>EDIT: Complete script below. Sorry about the length. This is being run as</p><pre><code>tshark -q -l -Xlua_script:extract.lua &quot;ip host W.X.Y.Z and tcp port NNNN&quot; &gt; client-X.pkts</code></pre><p>from a controller script that forks off one of these for each client (each client gets a different port; W.X.Y.Z, however, is always the public IP address of the machine running this script). When the client terminates, the tshark process is killed (with SIGTERM). <em>Thousands</em> of packets are being lost from the log -- I know by construction that each client generates tens of megabytes of traffic, at least, but often the .pkts file is empty!</p><p>Client and controller are running on (separate) Linux VMs, tshark -v says:</p><pre><code>TShark 1.10.2 (SVN Rev 51934 from /trunk-1.10)
...
Running on Linux 3.10-2-amd64, with locale en_US.utf8, with libpcap version
1.4.0, with libz 1.2.8.</code></pre><h3 id="complete-script">complete script:</h3><pre><code>do
   local function map(func, array)
      local new_array = {}
      for i,v in ipairs(array) do
         new_array[i] = func(v)
      end
      return new_array
   end

   -- http://ricilake.blogspot.com/2007/10/iterating-bits-in-lua.html
   local function hasbit(word, i)
      i = 2 ^ (i - 1)
      return word % (i + i) &gt;= i
   end

   local function decode_tcp_flags(flags)
      local labels = { -- counting from the low end up
         &quot;fin&quot;, &quot;syn&quot;, &quot;rst&quot;, &quot;psh&quot;, &quot;ack&quot;, &quot;urg&quot;,
         &quot;ece&quot;, &quot;cwr&quot;, &quot;ns&quot;,  &quot;rsv1&quot;,&quot;rsv2&quot;,&quot;rsv3&quot;
      }
      local decoded = &quot;&quot;
      for i, label in ipairs(labels) do
         if hasbit(flags, i) then
            if string.len(decoded) &gt; 0 then
               decoded = decoded .. &quot;.&quot;
            end
            decoded = decoded .. label
         end
      end
      return decoded
   end

   local rctypes = { [20] = &quot;cipher&quot;,
                     [21] = &quot;alert&quot;,
                     [22] = &quot;encrypted-handshake&quot;,
                     [23] = &quot;data&quot;,
                     [24] = &quot;heartbeat&quot; }

   local hstypes = { [0] = &quot;hello-request&quot;,
                     [1] = &quot;client-hello&quot;,
                     [2] = &quot;server-hello&quot;,
                     [3] = &quot;new-ticketed-session&quot;,
                     [11] = &quot;certificate&quot;,
                     [12] = &quot;server-key-exchange&quot;,
                     [13] = &quot;certificate-request&quot;,
                     [14] = &quot;server-done&quot;,
                     [15] = &quot;certificate-verify&quot;,
                     [16] = &quot;client-key-exchange&quot;,
                     [20] = &quot;finished&quot;,
                     [22] = &quot;certificate-status&quot;,
                     [67] = &quot;next-proto&quot; }

   local function decode_ssl_rctype(rctype, records)
      local label = rctypes[rctype]
      if label == nil then label = string.format(&quot;record-%d&quot;, rctype) end
      table.insert(records, label)
   end

   local function decode_ssl_hstype(hstype, records)
      local label = hstypes[hstype]
      if label == nil then label = string.format(&quot;handshake-%d&quot;, hstype) end
      local lastrecord = table.remove(records)
      if lastrecord ~= &quot;encrypted-handshake&quot; then
         table.insert(records, lastrecord)
      end
      table.insert(records, label)
   end

   local servers = {}
   local server_count = 0
   local function new_server(addr)
      local x = math.floor(server_count / 26) + 1
      local y = math.mod(server_count, 26) + 1

      local label = string.rep(string.sub(&quot;ABCDEFGHIJKLMNOPQRSTUVWXYZ&quot;,
                                          y, y), x)
      servers[addr] = label
      server_count = server_count + 1
      return label
   end

   local fieldnames = {
      &quot;tcp.len&quot;,
      &quot;udp.length&quot;,
      &quot;ip.src&quot;,
      &quot;ip.dst&quot;,
      &quot;tcp.srcport&quot;,
      &quot;tcp.dstport&quot;,
      &quot;udp.srcport&quot;,
      &quot;udp.dstport&quot;,
      &quot;tcp.flags&quot;,
      &quot;tcp.stream&quot;,
      &quot;tcp.analysis.retransmission&quot;,
      &quot;tcp.analysis.duplicate_ack&quot;,
      &quot;ssl.record.content_type&quot;,
      &quot;ssl.record.length&quot;,
      &quot;ssl.handshake.type&quot;
   }
   local dissectors = map(Field.new, fieldnames)

   local ip = Listener.new(&quot;ip&quot;)
   function ip.packet(pinfo, tvb)
      local number      = tonumber(pinfo.number)
      local time        = tonumber(pinfo.abs_ts)
      local packet_len  = tonumber(pinfo.len)
      local stream      = 0
      local proto       = &quot;udp&quot;
      local flags       = &quot;&quot;
      local dupe        = false
      local payload_len = 0
      local srcip       = nil
      local dstip       = nil
      local srcport     = nil
      local dstport     = nil
      local direction   = nil
      local host        = nil
      local port        = nil
      local sslrecords  = {}
      local sslreclens  = {}

      local fieldlist = { all_field_infos() }
      for ix, finfo in ipairs(fieldlist) do
         if finfo.name == &quot;ip.src&quot; then
            srcip = tostring(finfo.value)

         elseif finfo.name == &quot;ip.dst&quot; then
            dstip = tostring(finfo.value)

         elseif (finfo.name == &quot;tcp.srcport&quot; or
                 finfo.name == &quot;udp.srcport&quot;) then
            srcport = tonumber(finfo.value)

         elseif (finfo.name == &quot;tcp.dstport&quot; or
                 finfo.name == &quot;udp.dstport&quot;) then
            dstport = tonumber(finfo.value)

         elseif (finfo.name == &quot;tcp.len&quot; or
                 finfo.name == &quot;udp.length&quot;) then
            payload_len = tonumber(finfo.value)

         elseif finfo.name == &quot;tcp.stream&quot; then
            proto = &quot;tcp&quot;
            stream = tonumber(finfo.value) + 1

         elseif finfo.name == &quot;tcp.flags&quot; then
            flags = decode_tcp_flags(tonumber(finfo.value))

         elseif (finfo.name == &quot;tcp.analysis.retransmission&quot; or
                 finfo.name == &quot;tcp.analysis.duplicate_ack&quot;) then
            dupe = true

         elseif finfo.name == &quot;ssl.record.content_type&quot; then
            decode_ssl_rctype(tonumber(finfo.value), sslrecords)

         elseif finfo.name == &quot;ssl.handshake.type&quot; then
            decode_ssl_hstype(tonumber(finfo.value), sslrecords)

         elseif finfo.name == &quot;ssl.record.length&quot; then
            table.insert(sslreclens, tonumber(finfo.value))

         end
      end

      host = servers[srcip..&quot;:&quot;..srcport]
      if host ~= nil then
         direction = &quot;down&quot;
         port = srcport
      else
         host = servers[dstip..&quot;:&quot;..dstport]
         if host == nil then host = new_server(dstip..&quot;:&quot;..dstport) end
         direction = &quot;up&quot;
         port = dstport
      end

      if dupe then
         if flags == &quot;&quot;
         then flags = &quot;dup&quot;
         else flags = flags .. &quot;.dup&quot;
         end
      end

      sslrecords = table.concat(sslrecords, &quot;.&quot;)
      sslreclens = table.concat(sslreclens, &quot;.&quot;)
      io.write(string.format(&quot;%d:%d:%.6f:%s:%s:%s:%d:%s:%s:%d:%d:%s\n&quot;,
                             number,
                             stream,
                             time,
                             proto,
                             direction,
                             host,
                             port,
                             flags,
                             sslrecords,
                             packet_len,
                             payload_len,
                             sslreclens))
      io.flush()
   end
end</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '13, 15:42</strong></p><img src="https://secure.gravatar.com/avatar/dd7cc06b1b1c347e172c6ba532937173?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zack&#39;s gravatar image" /><p><span>Zack</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zack has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Sep '13, 07:45</strong> </span></p></div></div><div id="comments-container-24785" class="comments-container"><span id="24801"></span><div id="comment-24801" class="comment"><div id="post-24801-score" class="comment-score"></div><div class="comment-text"><p>can you please add the 'full' Lua code, in order to test it?</p><p>BTW: How did you notice that some packet are <strong>not</strong> being printed?</p><p>BTW#2: What is your OS and Wireshark version?</p></div><div id="comment-24801-info" class="comment-info"><span class="comment-age">(17 Sep '13, 03:21)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="24828"></span><div id="comment-24828" class="comment"><div id="post-24828-score" class="comment-score"></div><div class="comment-text"><p>@KurtKnochner Code and more detail about usage added. I hope this answers all your questions.</p></div><div id="comment-24828-info" class="comment-info"><span class="comment-age">(17 Sep '13, 07:43)</span> <span class="comment-user userinfo">Zack</span></div></div></div><div id="comment-tools-24785" class="comment-tools"></div><div class="clear"></div><div id="comment-24785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

