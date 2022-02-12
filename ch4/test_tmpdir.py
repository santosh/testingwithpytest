def test__tmpdir(tmpdir):
    # tmpdir already has a path name associated with it
    # join() extends the path to include a filename
    # the file is created when it's written to
    a_file = tmpdir.join("something.txt")

    # you can create directories
    a_sub_dir = tmpdir.mkdir("anything")

    # you can create files in directories (created when writeen)
    another_file = a_sub_dir.join("something_else.txt")

    # this write creates 'something.txt'
    a_file.write("contents may settle during shipping")

    # this wirte creates 'anything/something_else.txt'
    another_file.write("something different")

    # you can read the files as well
    assert a_file.read() == "contents may settle during shipping"
    assert another_file.read() == "something different"


def test__tmpdir_factory(tmpdir_factory):
    # you should start with makinga directory
    # a_dir acts like the object returned from the tmpdir fixture
    a_dir = tmpdir_factory.mktemp("mydir")

    # base_temp will be the parent dir of 'mydir'
    # you don't haveto use getbasetemp()
    # using it here just to showthat it's available
    base_temp = tmpdir_factory.getbasetemp()
    print("base: ", base_temp)

    # you can create files in directories (created when writeen)
    a_file = a_dir.join("something.txt")
    a_sub_dir = a_dir.mkdir("anything")
    another_file = a_sub_dir.join("something_else.txt")

    a_file.write("contents may settle during shipping")
    another_file.write("something different")

    assert a_file.read() == "contents may settle during shipping"
    assert another_file.read() == "something different"
