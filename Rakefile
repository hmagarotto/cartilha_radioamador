namespace :book do

  BOOK_FILE_NAME = 'cartilha_radioamador'
  CONTRIBUTORS_FILE_NAME = 'src/preface/contributors.txt'


  # Mapeia as variantes do livro para suas respectivas features.
  # Chave: Nome da variante (ex: 'default', 'ext')
  # Valor: Array de strings contendo as funcionalidades ou seções incluídas.
  VARIANTS = {
    "default" =>[],
    "fix"     => ["fix"],
    "ext"     => ["fix", "extended"],
  }

  # Variables referenced for build
  version_string = `git describe --tags --abbrev=0`.chomp
  if version_string.empty?
    version_string = '0'
  else
    versions = version_string.split('.')
    version_string = versions[0] + '.' + versions[1] + '.' + versions[2].to_i.next.to_s
  end
  date_string = Time.now.strftime('%Y-%m-%d')
  params = "--attribute revnumber='#{version_string}' --attribute revdate='#{date_string}'"
  header_hash = `git rev-parse --short HEAD`.strip

  # Create filenames for different extensions and variations
  def create_file_name(extension, variant)
    "#{BOOK_FILE_NAME}#{variant == 'default' ? '' : '_' + variant}.#{extension}"
  end

  def get_variant_params(variant)
    variant_params = ["--attribute variant-#{variant}"]
    VARIANTS[variant].each do |feature|
      variant_params << "--attribute enable-#{feature}"
    end
    variant_params.join(" ")
  end

  # Check contributors list
  # This checks commit hash stored in the header of list against current HEAD
  def check_contrib
    if File.exist?(CONTRIBUTORS_FILE_NAME)
      current_head_hash = `git rev-parse --short HEAD`.strip
      header = `head -n 1 #{CONTRIBUTORS_FILE_NAME}`.strip
      # Match regex, then coerce resulting array to string by join
      header_hash = header.scan(/[a-f0-9]{7,}/).join

      if header_hash == current_head_hash
        puts "Hash on header of contributors list (#{header_hash}) matches the current HEAD (#{current_head_hash})"
      else
        puts "Hash on header of contributors list (#{header_hash}) does not match the current HEAD (#{current_head_hash}), refreshing"
        sh "rm #{CONTRIBUTORS_FILE_NAME}"
        # Reenable and invoke task again
        Rake::Task[CONTRIBUTORS_FILE_NAME].reenable
        Rake::Task[CONTRIBUTORS_FILE_NAME].invoke
      end
    end
  end

  desc 'build basic book formats'
  task :build => [:build_html, :build_epub, :build_fb2, :build_mobi, :build_pdf] do
    begin
        # Run check
        Rake::Task['book:check'].invoke

        # Rescue to ignore checking errors
        rescue => e
        puts e.message
        puts 'Error when checking books (ignored)'
    end
  end

  desc 'build basic book formats (for ci)'
  task :ci => [:build_html, :build_epub, :build_fb2, :build_mobi, :build_pdf] do
      # Run check, but don't ignore any errors
      Rake::Task['book:check'].invoke
  end

  desc 'generate contributors list'
  file "#{CONTRIBUTORS_FILE_NAME}" do
      puts 'Generating contributors list'
      sh "echo 'Contribuidores a partir de #{header_hash}:\n' > #{CONTRIBUTORS_FILE_NAME}"
      sh "git shortlog -s HEAD | grep -v -E '(dependabot)' | cut -f 2- | sort | column -c 120 >> #{CONTRIBUTORS_FILE_NAME}"
  end

  desc 'build HTML format'
  task :build_html => "#{CONTRIBUTORS_FILE_NAME}" do
      check_contrib()

      VARIANTS.each_key do |variant|
        puts "Converting to HTML(#{variant})..."
        sh "bundle exec asciidoctor #{params} #{get_variant_params(variant)} -a data-uri -o '#{create_file_name('html', variant)}' src/index.asc"
        puts " -- HTML(#{variant}) generated"
      end

  end

  desc 'build Epub format'
  task :build_epub => "#{CONTRIBUTORS_FILE_NAME}" do
      check_contrib()

      VARIANTS.each_key do |variant|
        puts "Converting to EPub(#{variant})..."
        sh "bundle exec asciidoctor-epub3 #{params} #{get_variant_params(variant)} -o '#{create_file_name('epub', variant)}' src/index.asc"
        puts " -- Epub(#{variant}) generated"
      end

  end

  desc 'build FB2 format'
  task :build_fb2 => "#{CONTRIBUTORS_FILE_NAME}" do
      check_contrib()

      VARIANTS.each_key do |variant|
        puts "Converting to FB2(#{variant})..."
        sh "bundle exec asciidoctor-fb2 #{params} #{get_variant_params(variant)} -o '#{create_file_name('fb2.zip', variant)}' src/index.asc"
        puts " -- FB2(#{variant}) generated"
      end

  end

  desc 'build Mobi format'
  task :build_mobi => "#{CONTRIBUTORS_FILE_NAME}" do
      check_contrib()

      VARIANTS.each_key do |variant|
        puts "Converting to Mobi(#{variant})..."
        sh "bundle exec asciidoctor-epub3 #{params} #{get_variant_params(variant)} -a ebook-format=kf8 -o '#{create_file_name('mobi', variant)}' src/index.asc"
        puts " -- Mobi(#{variant}) generated"
      end
  end

  desc 'build PDF format'
  task :build_pdf => "#{CONTRIBUTORS_FILE_NAME}" do
      check_contrib()

      VARIANTS.each_key do |variant|
        puts "Converting to PDF(#{variant})... (this one takes a while)"
        sh "bundle exec asciidoctor-pdf #{params} #{get_variant_params(variant)} -o '#{create_file_name('pdf', variant)}' src/index.asc 2>/dev/null"
        puts " -- PDF(#{variant}) generated"
      end

  end

  desc 'Check generated books'
  task :check => [:build_html, :build_epub] do
      puts 'Checking generated books'

      VARIANTS.each_key do |variant|
        # sh "htmlproofer '#{create_file_name('html', variant)}'"
        # sh "epubcheck '#{create_file_name('epub', variant)}'"
      end
  end

  desc 'Clean all generated files'
  task :clean do
    begin
        puts 'Removing generated files'

        FileList[CONTRIBUTORS_FILE_NAME, 'cartilha_radioamador*.{html,epub,fb2.zip,mobi,pdf}'].each do |file|
            rm file

            # Rescue if file not found
            rescue Errno::ENOENT => e
              begin
                  puts e.message
                  puts 'Error removing files (ignored)'
              end
        end
    end
  end

end

task :default => "book:build"
